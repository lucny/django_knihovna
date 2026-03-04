# Cvičný úkol A — nový model `Vypujcka`

## Cíl cvičení
Procvičit práci s úplně novým modelem, který se do knihovní aplikace reálně hodí.

Student si má samostatně procvičit:
- návrh modelu s vazbami 1:N,
- práci s datem/časem (`DateField`, `DateTimeField`),
- použití `choices`, `default`, `help_text`, `error_messages`,
- validaci konzistence dat (`clean`),
- migrace a testovací data.

---

## Zadání
V aplikaci `knihovna` vytvořte nový model `Vypujcka`, který bude reprezentovat zapůjčení knihy čtenářem.

Model musí splňovat:

1. Model dědí z `models.Model`.
2. Pole `kniha` je `ForeignKey` na model `Kniha`.
3. Pole `ctenar` je `ForeignKey` na uživatele (`settings.AUTH_USER_MODEL`).
  - Vybírejte uživatele ze skupiny `readers`.
4. Pole `datum_vypujcky` je `DateField` s výchozí hodnotou aktuálního data.
5. Pole `termin_vraceni` je `DateField` (povinné).
6. Pole `stav` je `CharField` s `choices`:
   - `vypujceno`
   - `vraceno`
   - `po_terminu`
   a výchozí hodnotou `vypujceno`.
7. Pole `poznamka` je nepovinné (`TextField`).
8. Pole `upraveno` je `DateTimeField(auto_now=True)`.
9. V `Meta` nastavte řazení od nejnovější výpůjčky (`-datum_vypujcky`) a pak podle termínu vrácení.
10. Doplňte metodu `__str__`, která vrátí čitelně: čtenář, titul knihy, stav.
11. Přidejte metodu `clean`, která zkontroluje, že `termin_vraceni` není dřív než `datum_vypujcky`.
12. V `clean` doplňte i kontrolu, že vybraný čtenář je ve skupině `readers`.
13. Proveďte migrace a vytvořte alespoň 3 testovací záznamy (různé stavy).

---

## Povinné výstupy (co odevzdat)
- Upravený soubor `knihovna/models.py`.
- Nový migrační soubor ve složce `knihovna/migrations/`.
- Krátký screenshot nebo textový výstup ze shellu, kde je vidět:
  - `Vypujcka.objects.all()`
  - správné řazení dle data výpůjčky.

---

## Kontrolní kritéria (sebehodnocení)
Student má hotovo, pokud:
- [ ] lze vytvořit výpůjčku bez chyby,
- [ ] `stav` je výběr (ne libovolný text),
- [ ] `datum_vypujcky` se předvyplní,
- [ ] validace v `clean` zabrání nesmyslnému termínu vrácení,
- [ ] výpis výpůjček je od nejnovějších.

---

## Rozšiřující výzva (pro rychlejší studenty)
Zaveďte pravidlo: jedna kniha může mít současně jen jednu aktivní výpůjčku ve stavu `vypujceno`.

Nápověda:
- můžete řešit přes dodatečnou validační logiku v `clean`,
- nebo přes podmíněný constraint.

Dokumentace Django 6.0:
https://docs.djangoproject.com/en/6.0/ref/models/constraints/

---

## Nápověda k řešení
Pokud si nejste jistí syntaxí:
- modely: https://docs.djangoproject.com/en/6.0/topics/db/models/
- pole modelů: https://docs.djangoproject.com/en/6.0/ref/models/fields/
- AUTH_USER_MODEL: https://docs.djangoproject.com/en/6.0/topics/auth/customizing/#referencing-the-user-model
- validace modelu (`clean`): https://docs.djangoproject.com/en/6.0/ref/models/instances/#django.db.models.Model.clean
- migrace: https://docs.djangoproject.com/en/6.0/topics/migrations/

