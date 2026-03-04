from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Autor(models.Model):
    jmeno = models.CharField(max_length=80, verbose_name='Jméno autora', help_text='Zadejte jméno autora',
                             error_messages={'blank': 'Jméno autora musí být vyplněno'})
    prijmeni = models.CharField(max_length=50, verbose_name='Příjmení autora', help_text='Zadejte příjmení autora',
                                error_messages={'blank': 'Příjmení autora musí být vyplněno'})
    narozeni = models.DateField(blank=True, null=True, verbose_name='Datum narození')
    umrti = models.DateField(blank=True, null=True, verbose_name='Datum úmrtí')
    biografie = models.TextField(blank=True, verbose_name='Životopis')
    fotografie = models.ImageField(upload_to='autori', verbose_name='Fotografie')

    class Meta:
        ordering = ['prijmeni', 'jmeno']
        verbose_name = 'Autor'
        verbose_name_plural = 'Autoři'

    def __str__(self):
        return f'{self.jmeno} {self.prijmeni}'


class Zanr(models.Model):
    nazev = models.CharField(max_length=20, verbose_name='Název žánru', help_text='Zadejte název žánru')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Žánr'
        verbose_name_plural = 'Žánry'

    def __str__(self):
        return f'{self.nazev}'


class Vydavatelstvi(models.Model):
    nazev = models.CharField(max_length=100, verbose_name='Název vydavatelství', help_text='Zadejte název vydavatelství',
                             error_messages={'blank': 'Název vydavatelství je povinný údaj'})
    adresa = models.CharField(blank=True, null=True, max_length=200, verbose_name='Adresa')

    class Meta:
        ordering = ['nazev']
        verbose_name = 'Vydavatelství'
        verbose_name_plural = 'Vydavatelství'

    def __str__(self):
        return f'{self.nazev}'


class Kniha(models.Model):
    titul = models.CharField(max_length=100, verbose_name='Titul knihy', help_text='Zadejte titul knihy',
                             error_messages={'blank': 'Titul knihy musí být vyplněn'})
    autori = models.ManyToManyField(Autor)
    obsah = models.TextField(blank=True, verbose_name='Obsah knihy', help_text='Vložte obsah knihy')
    pocet_stran = models.PositiveIntegerField(blank=True, null=True, validators=[MaxValueValidator(9999)],
                                              verbose_name='Počet stran', help_text='Zadejte počet stran (max. 9999)')
    rok_vydani = models.PositiveIntegerField(blank=True, null=True, validators=[MinValueValidator(1500), MaxValueValidator(2100)],
                                             verbose_name='Rok vydání', help_text='Zadejte rok vydání (1500 - 2100)')
    obalka = models.ImageField(upload_to='obalky', verbose_name='Obálka knihy')
    zanry = models.ManyToManyField(Zanr)
    vydavatelstvi = models.ForeignKey('Vydavatelstvi', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Vydavatelství')

    class Meta:
        ordering = ['titul']
        verbose_name = 'Kniha'
        verbose_name_plural = 'Knihy'

    def __str__(self):
        return f'{self.titul} ({self.rok_vydani})'


class Recenze(models.Model):
    HODNOCENI_CHOICES = (
        (0, '☆☆☆☆☆'),
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★'),
    )

    recenzent = models.ForeignKey(
        Autor,
        on_delete=models.CASCADE,
        related_name='recenze',
        verbose_name='Recenzent',
        help_text='Vyberte recenzenta',
        error_messages={'blank': 'Recenzent musí být vybrán'}
    )
    kniha = models.ForeignKey(
        Kniha,
        on_delete=models.CASCADE,
        related_name='recenze',
        verbose_name='Kniha',
        help_text='Vyberte recenzovanou knihu',
        error_messages={'blank': 'Kniha musí být vybrána'}
    )
    text = models.TextField(
        verbose_name='Text recenze',
        help_text='Napište text recenze',
        error_messages={'blank': 'Text recenze je povinný'}
    )
    hodnoceni = models.IntegerField(
        choices=HODNOCENI_CHOICES,
        default=3,
        verbose_name='Hodnocení',
        help_text='Vyberte hodnocení od 0 do 5'
    )
    upraveno = models.DateTimeField(
        auto_now=True,
        verbose_name='Naposledy upraveno',
        help_text='Datum poslední úpravy se nastavuje automaticky'
    )

    class Meta:
        ordering = ['-hodnoceni']
        verbose_name = 'Recenze'
        verbose_name_plural = 'Recenze'

    def __str__(self):
        hvezdy = dict(self.HODNOCENI_CHOICES).get(self.hodnoceni, '')
        return f'{self.recenzent} | {self.text[:40]} | {self.upraveno:%d.%m.%Y %H:%M} | {hvezdy}'


class Vypujcka(models.Model):
    # Choices držíme jako konstantu přímo v modelu, aby byly na jednom místě
    # pro formuláře, admin i případné validace.
    STAV_VYPUJCENO = 'vypujceno'
    STAV_VRACENO = 'vraceno'
    STAV_PO_TERMINU = 'po_terminu'
    STAV_CHOICES = (
        (STAV_VYPUJCENO, 'Vypůjčeno'),
        (STAV_VRACENO, 'Vráceno'),
        (STAV_PO_TERMINU, 'Po termínu'),
    )

    # ForeignKey představuje vazbu 1:N (jedna kniha může mít více historických výpůjček).
    kniha = models.ForeignKey(
        Kniha,
        on_delete=models.CASCADE,
        related_name='vypujcky',
        verbose_name='Kniha',
        help_text='Vyberte knihu, která je půjčená.'
    )
    ctenar = models.CharField(
        max_length=120,
        verbose_name='Čtenář',
        help_text='Zadejte jméno a příjmení čtenáře.',
        error_messages={'blank': 'Čtenář musí být vyplněn.'}
    )
    # timezone.localdate vrací datum v lokálním časovém pásmu Django projektu.
    datum_vypujcky = models.DateField(
        default=timezone.localdate,
        verbose_name='Datum výpůjčky',
        help_text='Datum, kdy byla kniha zapůjčena.'
    )
    termin_vraceni = models.DateField(
        verbose_name='Termín vrácení',
        help_text='Nejzazší datum, do kdy má být kniha vrácena.',
        error_messages={'blank': 'Termín vrácení je povinný.'}
    )
    stav = models.CharField(
        max_length=20,
        choices=STAV_CHOICES,
        default=STAV_VYPUJCENO,
        verbose_name='Stav výpůjčky',
        help_text='Aktuální stav výpůjčky.'
    )
    poznamka = models.TextField(
        blank=True,
        verbose_name='Poznámka',
        help_text='Volitelná poznámka (poškození, domluva o prodloužení, ...).'
    )
    upraveno = models.DateTimeField(auto_now=True, verbose_name='Naposledy upraveno')

    class Meta:
        ordering = ['-datum_vypujcky', 'termin_vraceni']
        verbose_name = 'Výpůjčka'
        verbose_name_plural = 'Výpůjčky'

    def __str__(self):
        return f'{self.ctenar} | {self.kniha.titul} | {self.get_stav_display()}'

    def clean(self):
        # business pravidlo ze zadání: termín vrácení nesmí být dříve
        # než samotné datum výpůjčky.
        if self.termin_vraceni and self.datum_vypujcky and self.termin_vraceni < self.datum_vypujcky:
            raise ValidationError({'termin_vraceni': 'Termín vrácení nesmí být dříve než datum výpůjčky.'})

        # rozšiřující výzva: u jedné knihy povolíme jen jednu aktivní výpůjčku.
        # Vyloučíme vlastní záznam (self.pk), aby šla výpůjčka bez problému upravit.
        aktivni_vypujcka_existuje = (
            Vypujcka.objects
            .filter(kniha=self.kniha, stav=self.STAV_VYPUJCENO)
            .exclude(pk=self.pk)
            .exists()
        )
        if self.kniha_id and self.stav == self.STAV_VYPUJCENO and aktivni_vypujcka_existuje:
            raise ValidationError({'stav': 'Tato kniha už má aktivní výpůjčku.'})

    def je_po_terminu(self):
        # Metoda vrací bool, aby se dala použít jak v šabloně, tak v adminu.
        dnes = timezone.localdate()
        return self.stav != self.STAV_VRACENO and self.termin_vraceni < dnes

    def aktualizuj_stav(self, ulozit=True):
        # Přepočítá stav objektu podle termínu.
        # Pokud je výpůjčka vrácená, stav už neměníme.
        if self.stav != self.STAV_VRACENO and self.je_po_terminu():
            self.stav = self.STAV_PO_TERMINU
            if ulozit:
                self.save(update_fields=['stav', 'upraveno'])
