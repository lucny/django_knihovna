# Cvičný úkol E — detail výpůjčky

## Návaznost
Navazuje na [ukol-d.md](ukol-d.md).

## Cíl cvičení
Vytvořit detailovou stránku jedné výpůjčky a procvičit bezpečné načítání objektu podle ID.

---

## Zadání
Vytvořte stránku detailu výpůjčky na adrese `/knihovna/loans/<id>/`.

Stránka má zobrazit:
- čtenáře,
- detail knihy (titul + odkaz na detail knihy),
- stav výpůjčky,
- datum výpůjčky,
- termín vrácení,
- poznámku.

Požadavky:
1. Použijte `get_object_or_404`.
2. Přidejte tlačítko „Zpět na seznam výpůjček“.
3. Přidejte odkaz z tabulky v úkolu D na tento detail.

---

## Povinné výstupy
- Nový detail view.
- Nová detail šablona.
- Funkční provázání list → detail.

---

## Kontrolní kritéria
- [ ] existující ID vrací detail,
- [ ] neexistující ID vrací 404,
- [ ] navigace zpět funguje,
- [ ] stránka používá data z modelu `Vypujcka` bez duplikace logiky.

---

## Nápověda
- Shortcuts (`get_object_or_404`): https://docs.djangoproject.com/en/6.0/topics/http/shortcuts/
