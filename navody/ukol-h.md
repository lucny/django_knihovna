# Cvičný úkol H — optimalizace a čistota `views.py`

## Návaznost
Navazuje na view z úkolů D–G.

## Cíl cvičení
Naučit se upravit pohledy tak, aby byly:
- čitelné,
- výkonné,
- snadno testovatelné.

---

## Zadání
Refaktorujte pohledy pro výpůjčky a čtenáře:

1. Použijte `select_related`/`prefetch_related` tam, kde to dává smysl.
2. Omezte logiku v šablonách — složitější výpočty přeneste do view.
3. Ve všech detailových pohledech používejte `get_object_or_404`.
4. Přidejte stručné docstringy ke každému novému view.
5. Upravte názvy proměnných v kontextu tak, aby byly konzistentní (`loan`, `loans`, `reader`, `reader_loans`).

---

## Povinné výstupy
- Refaktorovaný `knihovna/views.py`.
- Krátké zdůvodnění (3–5 vět), co jste optimalizovali a proč.

---

## Kontrolní kritéria
- [ ] stránky se chovají stejně jako před refaktorem,
- [ ] view jsou čitelnější než předtím,
- [ ] nevznikly nové chyby v routech nebo šablonách,
- [ ] práce s DB je efektivnější.

---

## Nápověda
- Query optimizations: https://docs.djangoproject.com/en/6.0/topics/db/optimization/
