# Cvičný úkol D — stránka „Seznam výpůjček“

## Návaznost
Navazuje na [ukol-c.md](ukol-c.md) a používá data modelu `Vypujcka`.

## Cíl cvičení
Vytvořit první veřejnou stránku nad modelem `Vypujcka`.

---

## Zadání
Vytvořte novou stránku na adrese `/knihovna/loans/`, která zobrazí tabulku výpůjček.

Tabulka musí obsahovat sloupce:
- Čtenář
- Kniha (odkaz na detail knihy)
- Stav
- Datum výpůjčky
- Termín vrácení

Požadavky:
1. Výpis je řazen od nejnovějších výpůjček.
2. Řádek po termínu má vizuální zvýraznění (např. Bootstrap `table-danger`).
3. U vrácených výpůjček se zvýraznění nepoužije.

---

## Povinné výstupy
- Nový view ve `views.py`.
- Nová šablona (např. `loans_list.html`).
- Funkční URL `/knihovna/loans/`.

---

## Kontrolní kritéria
- [ ] stránka se načte bez chyby,
- [ ] odkazy na detail knihy fungují,
- [ ] zvýraznění odpovídá skutečnému stavu výpůjčky,
- [ ] data jsou čitelná i na mobilu.

---

## Nápověda
- QuerySet API: https://docs.djangoproject.com/en/6.0/ref/models/querysets/
- Templates: https://docs.djangoproject.com/en/6.0/topics/templates/
