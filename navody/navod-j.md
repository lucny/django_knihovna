# Návod J — validní HTML a přehledný zdrojový kód

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
Systematicky ověřit, že řešení je:
- funkční,
- čitelné,
- validní.

## Postup krok za krokem

---

## Krok 1: Proveďte technickou kontrolu Django

### Kód pro tento krok

```bash
python manage.py check
python manage.py makemigrations --check
```

### Vysvětlení
- `check`: statická kontrola nastavení, modelů a projektu.
- `makemigrations --check`: ověří, že nechybí migrace.

### Ověření kroku
Krok je hotový, když oba příkazy skončí bez chybového hlášení.

---

## Krok 2: Otestujte všechny URL

### Kód pro tento krok

```bash
python manage.py runserver
```

Otevřete a zkontrolujte:
- `http://127.0.0.1:8000/knihovna/`
- `http://127.0.0.1:8000/knihovna/books/`
- `http://127.0.0.1:8000/knihovna/books/1/`
- `http://127.0.0.1:8000/knihovna/authors/`
- `http://127.0.0.1:8000/knihovna/authors/1/`
- `http://127.0.0.1:8000/books/1/`

### Co musí platit
- žádná stránka nevrací 500,
- neexistující ID vrací 404,
- odkazy v navigaci fungují.

### Vysvětlení
Tento krok je integrační test — ověřuje, že modely, view, URL i šablony spolupracují.

### Ověření kroku
Krok je hotový, když všechny uvedené URL splní tři podmínky výše.

---

## Krok 3: Zkontrolujte validitu HTML

### Kód pro tento krok
Není to shell příkaz, ale checklist pro každou šablonu:

```text
1) Tagy jsou správně uzavřené.
2) Obrázky mají alt atribut.
3) Odkazy nesměřují na #, pokud stránka existuje.
4) Stránka má logickou strukturu nadpisů.
```

### Vysvětlení
HTML validita přímo ovlivňuje zobrazení, přístupnost i výsledné hodnocení úlohy.

### Dokumentace
- Šablony Django: https://docs.djangoproject.com/en/6.0/topics/templates/
- HTML validátor W3C: https://validator.w3.org/

### Ověření kroku
Krok je hotový, když validátor nehlásí kritické HTML chyby.

---

## Krok 4: Zkontrolujte čitelnost Python kódu

### Kód pro tento krok
Opět checklist:

```text
1) 4 mezery odsazení.
2) Importy nahoře v souboru.
3) Smysluplné názvy funkcí a proměnných.
4) Bez duplicitního kódu.
5) Detailové pohledy používají get_object_or_404.
```

### Vysvětlení
Tento checklist drží kvalitu zdrojového kódu a usnadňuje následné hodnocení i údržbu.

### Ověření kroku
Krok je hotový, když všechny body checklistu platí pro upravené soubory.

---

## Typické chyby studentů a jak je poznat

- **Přeskočení `python manage.py check`**: problémy se objeví až při klikání v aplikaci.
- **Neotestované hraniční URL (neexistující ID)**: 404/500 chyby zůstanou neodhalené.
- **Nevalidní HTML v šablonách**: rozpad layoutu nebo problémy s přístupností.
- **Odkazy ponechané jako `#`**: navigace vypadá hotově, ale není funkční.
- **Nekonzistentní styl kódu**: horší čitelnost a složitější hodnocení projektu.

---

## Rychlá diagnostika (když něco nefunguje)

1. Vždy začněte `python manage.py check`.
2. Pak spusťte server a testujte URL systematicky podle seznamu v tomto návodu.
3. Chyby `TemplateDoesNotExist` řešte kontrolou názvu a umístění šablon.
4. Chyby `NoReverseMatch` řešte porovnáním `name=...` v URL a `{% url %}` v šabloně.
5. U 500 chyb vždy čtěte první řádky tracebacku — obvykle ukážou přesný soubor a problém.

---

## Kompletní kontrolní postup (souhrn)

```bash
python manage.py check
python manage.py makemigrations --check
python manage.py runserver
```

Pak ručně projděte URL a checklist z kroků 3 a 4.
