# Cvičný úkol B — rozšíření modelu `Vypujcka` (Meta, `__str__`, logika stavu)

## Návaznost
Navazuje na [ukol-a.md](ukol-a.md), kde byl vytvořen základ modelu `Vypujcka`.

## Cíl cvičení
Prohloubit práci s modelem:
- správné řazení přes `Meta`,
- čitelná reprezentace objektu,
- zapouzdření logiky do metod modelu.

---

## Zadání
V modelu `Vypujcka` doplňte:

1. `class Meta`:
   - `ordering = ['-datum_vypujcky', 'termin_vraceni']`
   - `verbose_name = 'Výpůjčka'`
   - `verbose_name_plural = 'Výpůjčky'`
2. Metodu `__str__`, která vrátí čitelně:
   - čtenáře,
   - titul knihy,
   - aktuální stav.
3. Metodu `je_po_terminu(self)`, která vrací `True/False` podle toho, zda je dnes po termínu vrácení a výpůjčka není vrácená.
4. Metodu `aktualizuj_stav(self)`, která nastaví `stav='po_terminu'`, pokud je výpůjčka po termínu.

---

## Povinné výstupy
- Upravený `knihovna/models.py`.
- Ukázka ze shellu:
  - volání `je_po_terminu()`
  - volání `aktualizuj_stav()`
  - `Vypujcka.objects.all()` v očekávaném pořadí.

---

## Kontrolní kritéria
- [ ] řazení funguje automaticky bez ručního `order_by`,
- [ ] `__str__` je čitelné v adminu i shellu,
- [ ] logika stavu je v metodách modelu (ne v šabloně),
- [ ] po spuštění `aktualizuj_stav()` se stav správně změní.

---

## Nápověda
- Meta options: https://docs.djangoproject.com/en/6.0/ref/models/options/
- Model instance methods: https://docs.djangoproject.com/en/6.0/topics/db/models/#model-methods
