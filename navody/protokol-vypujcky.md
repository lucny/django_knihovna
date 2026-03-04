# Kontrolní protokol — modul výpůjček (A–J)

## Co bylo testováno
- Technická kontrola projektu (`check`, migrace).
- Funkčnost URL pro seznam/detail výpůjček.
- Funkčnost URL pro seznam/detail čtenářů.
- Chybové scénáře (`404` pro neexistující výpůjčku i čtenáře).
- Konzistence dat v modelu (`clean`, stav po termínu).

## Co prošlo
- `python manage.py check` bez chyb.
- `python manage.py makemigrations --check` bez neaplikovaných změn.
- `/knihovna/loans/` zobrazuje tabulku výpůjček, odkazy a zvýraznění po termínu.
- `/knihovna/loans/<id>/` vrací detail výpůjčky a tlačítko zpět.
- `/knihovna/readers/` vrací agregovaný přehled čtenářů.
- `/knihovna/readers/<slug>/` vrací detail čtenáře s jeho výpůjčkami.

## Co bylo opraveno
- Přidán nový model `Vypujcka` (včetně `clean`, `je_po_terminu`, `aktualizuj_stav`).
- Doplněna administrace modelu `Vypujcka` s filtrováním a vyhledáváním.
- Přidány view a URL pro `loans` a `readers`.
- Přidány nové šablony a UX úpravy (badge stavů, responzivní tabulky, aktivní navbar).

## Co zůstává k dopracování
- Volitelně přidat automatický seed skript pro testovací data do samostatného management commandu.
- Volitelně doplnit jednotkové testy pro slug mapování čtenářů a metodu `clean`.