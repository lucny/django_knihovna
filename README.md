# Django – Školní knihovna

Školní cvičný projekt postavený na Django. Repo obsahuje:
- základní knihovní aplikaci,
- podrobné návody k původním úlohám (`navod-a.md` až `navod-j.md`),
- navazující cvičné úkoly (`ukol-a.md` až `ukol-j.md`).

## Rychlé spuštění

1. Naklonujte repozitář:
	- `git clone https://github.com/lucny/django_knihovna.git`
2. Přejděte do projektu:
	- `cd django_knihovna`
3. Vytvořte virtuální prostředí:
	- `python -m venv .venv`
4. Aktivujte virtuální prostředí:
	- Windows PowerShell: `.venv\Scripts\Activate.ps1`
	- Linux/macOS: `source .venv/bin/activate`
5. Nainstalujte závislosti:
	- `pip install -r requirements.txt`
6. Proveďte migrace:
	- `python manage.py migrate`
7. Spusťte server:
	- `python manage.py runserver`

Projekt pak běží na `http://127.0.0.1:8000/`.

## Administrace

- URL: `http://127.0.0.1:8000/admin/`
- superuživatel: `admin`
- heslo: `admin`

## Struktura výukových materiálů

- Původní podrobné návody: [navody](navody)
  - `navod-a.md` až `navod-j.md`
- Procvičovací navazující úkoly: [navody](navody)
  - `ukol-a.md` až `ukol-j.md`

## Užitečné příkazy

- kontrola projektu: `python manage.py check`
- vytvoření migrací: `python manage.py makemigrations`
- Django shell: `python manage.py shell`

## Checklist po přepnutí větve

Po `git checkout` na jinou větev (např. `main` ↔ `ukoly`) vždy spusťte:

1. `python manage.py migrate`
2. `python manage.py check`
3. `python manage.py runserver`

Tím předejdete chybám typu `no such table` při načítání detailů knih, autorů nebo výpůjček.

## Řešení typických problémů při spuštění

### 1) Nejde aktivovat virtuální prostředí v PowerShellu

Projev:
- chyba o zakázaném spouštění skriptů.

Řešení:
- spusťte PowerShell jako uživatel a zadejte:
	- `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`
- pak znovu aktivujte:
	- `.venv\Scripts\Activate.ps1`

### 2) `ModuleNotFoundError` po spuštění `manage.py`

Projev:
- chybí balíček (např. Django, Pillow apod.).

Řešení:
- ověřte aktivní `.venv`,
- znovu nainstalujte závislosti:
	- `pip install -r requirements.txt`

### 3) Chyby migrací / neexistující tabulka

Projev:
- hlášky typu `no such table`, `OperationalError`, neaplikované migrace.

Řešení:
- spusťte:
	- `python manage.py makemigrations`
	- `python manage.py migrate`

### 4) Nezobrazují se obrázky nebo static soubory

Projev:
- chybí styly, loga nebo obrázky knih/autorů.

Řešení:
- ověřte, že běžíte v `DEBUG=True`,
- ověřte nastavení `STATIC_URL`, `MEDIA_URL`,
- zkontrolujte, že soubory skutečně existují ve složkách `knihovna/static` a `media`.

### 5) Port 8000 je obsazený

Projev:
- server nejde spustit na výchozím portu.

Řešení:
- spusťte server na jiném portu:
	- `python manage.py runserver 8001`

## Poznámka

Složka `media/` obsahuje runtime soubory (obrázky nahrané během běhu aplikace). Tyto soubory se standardně negenerují z kódu a typicky se necommitují.
