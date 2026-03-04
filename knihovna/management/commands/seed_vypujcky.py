from datetime import timedelta

from django.core.exceptions import ValidationError
from django.core.management.base import BaseCommand
from django.utils import timezone

from knihovna.models import Kniha, Vypujcka


class Command(BaseCommand):
    help = 'Vytvoří vzorová data pro model Vypujcka (minimálně 8 záznamů).'

    def handle(self, *args, **options):
        knihy = list(Kniha.objects.order_by('id')[:4])
        if not knihy:
            self.stdout.write(self.style.ERROR('Nelze vytvořit výpůjčky: v databázi nejsou žádné knihy.'))
            return

        dnes = timezone.localdate()
        # Data pokrývají všechny požadované scénáře:
        # - vypůjčeno
        # - vráceno
        # - po termínu
        vzorova_data = [
            ('Jan Novák', knihy[0], dnes - timedelta(days=2), dnes + timedelta(days=12), Vypujcka.STAV_VYPUJCENO),
            ('Eva Dvořáková', knihy[1 % len(knihy)], dnes - timedelta(days=20), dnes - timedelta(days=5), Vypujcka.STAV_PO_TERMINU),
            ('Petr Svoboda', knihy[2 % len(knihy)], dnes - timedelta(days=12), dnes - timedelta(days=1), Vypujcka.STAV_PO_TERMINU),
            ('Lucie Králová', knihy[3 % len(knihy)], dnes - timedelta(days=15), dnes - timedelta(days=2), Vypujcka.STAV_VRACENO),
            ('Tomáš Horák', knihy[0], dnes - timedelta(days=30), dnes - timedelta(days=20), Vypujcka.STAV_VRACENO),
            ('Anna Veselá', knihy[1 % len(knihy)], dnes - timedelta(days=17), dnes - timedelta(days=3), Vypujcka.STAV_VRACENO),
            ('Martin Kučera', knihy[2 % len(knihy)], dnes - timedelta(days=7), dnes + timedelta(days=5), Vypujcka.STAV_VRACENO),
            ('Karolína Němcová', knihy[3 % len(knihy)], dnes - timedelta(days=10), dnes + timedelta(days=4), Vypujcka.STAV_VYPUJCENO),
        ]

        vytvoreno = 0
        for ctenar, kniha, datum_vypujcky, termin_vraceni, stav in vzorova_data:
            # update_or_create drží command opakovatelný (idempotentní):
            # opakované spuštění neduplikuje řádky.
            vypujcka, created = Vypujcka.objects.update_or_create(
                ctenar=ctenar,
                kniha=kniha,
                defaults={
                    'datum_vypujcky': datum_vypujcky,
                    'termin_vraceni': termin_vraceni,
                    'stav': stav,
                    'poznamka': 'Vzorová data pro cvičné úkoly A–J.',
                },
            )

            # full_clean před save vynutí modelovou validaci i mimo formuláře.
            try:
                vypujcka.full_clean()
                vypujcka.save()
            except ValidationError:
                # Pokud by v DB už existovala jiná aktivní výpůjčka stejné knihy,
                # převedeme tento vzorový záznam na vrácený, aby data byla konzistentní.
                vypujcka.stav = Vypujcka.STAV_VRACENO
                vypujcka.full_clean()
                vypujcka.save(update_fields=['stav', 'datum_vypujcky', 'termin_vraceni', 'poznamka', 'upraveno'])

            if created:
                vytvoreno += 1

        self.stdout.write(self.style.SUCCESS(f'Hotovo. Nově vytvořeno {vytvoreno} výpůjček.'))
        self.stdout.write(f'Celkem v databázi: {Vypujcka.objects.count()} výpůjček.')