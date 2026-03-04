# Cvičný úkol F — přehled čtenářů z výpůjček

## Návaznost
Navazuje na [ukol-e.md](ukol-e.md) a stále používá model `Vypujcka`.

## Cíl cvičení
Procvičit agregace a seskupování dat nad uživateli (`User`) bez vytváření samostatného modelu čtenáře.

---

## Zadání
Vytvořte stránku `/knihovna/readers/`, která zobrazí přehled čtenářů odvozený z tabulky výpůjček.

Požadavky:
1. Každý čtenář se zobrazí pouze jednou.
2. U každého čtenáře ukažte:
   - počet všech výpůjček,
   - počet aktivních výpůjček (`stav='vypujceno'`),
   - počet výpůjček po termínu.
3. Každé jméno čtenáře odkazuje na `/knihovna/readers/<id>/` (ID uživatele).
4. Na detailu čtenáře zobrazte jeho výpůjčky v tabulce.

Poznámka: čtenář je uživatel (`User`), doporučeně člen skupiny `readers`.

---

## Povinné výstupy
- View pro seznam čtenářů a detail čtenáře.
- Dvě nové šablony.
- Funkční odkazy mezi stránkami.

---

## Kontrolní kritéria
- [ ] agregované počty sedí vůči datům v DB,
- [ ] detail čtenáře zobrazuje jen jeho výpůjčky,
- [ ] URL jsou stabilní a nevedou k 500 chybám,
- [ ] stránka je přehledná na desktopu i mobilu.


---

## Nápověda
- Aggregation: https://docs.djangoproject.com/en/6.0/topics/db/aggregation/
