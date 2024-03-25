from datetime import datetime, timedelta
import random
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from knihovna.models import Recenze

class Command(BaseCommand):
    help = 'Updates the "upraveno" field of reviews with random dates and times'

    def handle(self, *args, **kwargs):
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 3, 20)
        delta = end_date - start_date

        recenze_qs = Recenze.objects.all()

        for recenze in recenze_qs:
            random_number_of_days = random.randrange(delta.days)
            random_date = start_date + timedelta(days=random_number_of_days)
            random_time = (datetime.min + timedelta(seconds=random.randint(0, 86399))).time()
            random_datetime = datetime.combine(random_date, random_time)
            recenze.upraveno = make_aware(random_datetime)
            recenze.save()

        print(f'Časové údaje "upraveno" byly úspěšně aktualizovány pro {recenze_qs.count()} recenzí.')
