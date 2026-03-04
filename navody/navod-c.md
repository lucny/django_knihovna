# Návod C — migrace, registrace do adminu, testovací záznam

## Než začneš

1. Otevři terminál v kořeni projektu (`D:\django_knihovna`).
2. Aktivuj virtuální prostředí:
    - Windows PowerShell: `D:\django_knihovna\.venv\Scripts\Activate.ps1`
3. Ověř, že projekt běží:
    - `python manage.py runserver`
4. Pro rychlé testy modelů používej shell:
    - `python manage.py shell`
5. Když narazíš na chybu, začni kontrolou:
    - `python manage.py check`

---

## Cíl úlohy
Po vytvoření modelu `Recenze` provést:
1. registraci modelu v administraci,
2. migraci databáze,
3. vložení testovacího záznamu.

## Postup krok za krokem

---

## Krok 1: Zaregistrujte model `Recenze` do adminu

### Kód pro tento krok
Nahraďte `knihovna/admin.py`:

```python
from django.contrib import admin
from .models import Autor, Kniha, Vydavatelstvi, Zanr, Recenze

admin.site.register(Autor)
admin.site.register(Kniha)
admin.site.register(Vydavatelstvi)
admin.site.register(Zanr)
admin.site.register(Recenze)
```

### Vysvětlení
- `admin.site.register(Model)`: zpřístupní model v `/admin`.
- Import `Recenze` je nutný, jinak registrace nebude fungovat.

### Ověření kroku
Krok je hotový, když se model `Recenze` zobrazí v administraci.

Dokumentace adminu:
https://docs.djangoproject.com/en/6.0/ref/contrib/admin/

---

## Krok 2: Vytvořte migrace

### Kód pro tento krok

```bash
python manage.py makemigrations
```

### Vysvětlení
- `makemigrations` porovná modely a vytvoří migrační soubor.
- Nový soubor najdete v `knihovna/migrations/`.

### Ověření kroku
Krok je hotový, když vznikne nová migrace pro model `Recenze`.

Dokumentace migrací:
https://docs.djangoproject.com/en/6.0/topics/migrations/

---

## Krok 3: Aplikujte migrace

### Kód pro tento krok

```bash
python manage.py migrate
```

### Vysvětlení
- `migrate` provede SQL změny v databázi.
- Bez tohoto kroku model fyzicky v DB nevznikne.

### Ověření kroku
Krok je hotový, když příkaz `migrate` doběhne bez chyby.

---

## Krok 4: Vložte testovací recenzi přes shell

### Kód pro tento krok

```bash
python manage.py shell
```

```python
from django.contrib.auth import get_user_model
from knihovna.models import Kniha, Recenze

k_user = get_user_model()
uzivatel = k_user.objects.first()
kniha = Kniha.objects.first()

Recenze.objects.create(
    recenzent=uzivatel,
    kniha=kniha,
    text='Výborná kniha, doporučuji k přečtení.',
    hodnoceni=5
)
```

### Vysvětlení
- `recenzent`: objekt uživatele (`User`) — musí existovat v DB.
- `kniha`: objekt knihy (musí existovat v DB).
- `text`: povinný text recenze.
- `hodnoceni`: číslo z intervalu 0 až 5.

### Ověření kroku
Krok je hotový, když `create(...)` vrátí vytvořený objekt bez výjimky.

---

## Krok 5: Ověřte výsledek

### Kód pro tento krok

```python
Recenze.objects.all()
```

### Vysvětlení
Výpis všech recenzí je nejrychlejší kontrola, že migrace i vložení dat proběhly správně.

### Ověření kroku
- minimálně jeden objekt `Recenze`,
- textová reprezentace odpovídající úloze B.

---

## Typické chyby studentů a jak je poznat

- **Zapomenutý import `Recenze` v adminu**: aplikace hlásí `NameError` nebo model není v `/admin`.
- **Spuštěno jen `makemigrations` bez `migrate`**: model je v kódu, ale tabulka v DB neexistuje.
- **V shellu `get_user_model().objects.first()` vrací `None`**: `create(...)` selže, protože není vybraný recenzent.
- **Špatné pořadí příkazů**: po změně modelu se objevují neaplikované migrace.
- **Neověření výsledku**: chyba se projeví až v dalších úlohách při načítání recenzí.

---

## Rychlá diagnostika (když něco nefunguje)

1. Když model není v `/admin`, zkontrolujte `admin.py` (import + `register`).
2. Když je DB chyba „no such table“, spusťte `python manage.py migrate`.
3. Když `create(...)` padá, ověřte, že existuje uživatel i kniha (`get_user_model().objects.count()`, `Kniha.objects.count()`).
4. Po vložení dat vždy ověřte `Recenze.objects.all()`.
5. Pokud shell vrací nečekané chyby, ukončete ho a spusťte znovu po aktivaci `.venv`.

---

## Kompletní kód pro kontrolu

`knihovna/admin.py`:

```python
from django.contrib import admin
from .models import Autor, Kniha, Vydavatelstvi, Zanr, Recenze

admin.site.register(Autor)
admin.site.register(Kniha)
admin.site.register(Vydavatelstvi)
admin.site.register(Zanr)
admin.site.register(Recenze)
```

Příkazy v pořadí:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
