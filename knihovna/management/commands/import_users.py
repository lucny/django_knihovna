import csv
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Imports users from a CSV file'

    def handle(self, *args, **kwargs):
        # Cesta k souboru CSV
        file_path = 'knihovna/management/data/uzivatele.csv'

        # Načtení a zpracování CSV souboru
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                username, password, first_name, last_name, email = row
                if not User.objects.filter(username=username).exists():
                    User.objects.create_user(username=username, password=password, first_name=first_name,
                                             last_name=last_name, email=email)
                    print(f'Uživatel {username} byl úspěšně přidán.')
                else:
                    print(f'Uživatel {username} již existuje.')