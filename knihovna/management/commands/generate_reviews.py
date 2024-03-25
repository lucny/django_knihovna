import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from knihovna.models import Kniha, Recenze

class Command(BaseCommand):
    help = 'Generates fake reviews for books'

    def handle(self, *args, **kwargs):
        fake = Faker('cs_CZ')  # Pro generování v češtině
        users = User.objects.filter(id__range=(3, 12))  # Uživatelé s ID 3 až 12
        books = Kniha.objects.filter(id__range=(1, 22))  # Knihy s ID 1 až 22

        for _ in range(100):
            book = random.choice(books)
            user = random.choice(users)
            # Kontrola, zda už uživatel nenapsal recenzi na danou knihu
            if not Recenze.objects.filter(kniha=book, recenzent=user).exists():
                Recenze.objects.create(
                    text=fake.text(),
                    kniha=book,
                    recenzent=user,
                    hodnoceni=random.randint(1, 5)
                )
            else:
                print(f'Uživatel {user} již napsal recenzi na knihu {book}. Přeskakuji.')

        print('Recenze byly úspěšně vygenerovány.')
