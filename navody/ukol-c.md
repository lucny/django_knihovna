# Cvičný úkol C — administrace a testovací data pro `Vypujcka`

## Návaznost
Navazuje na [ukol-a.md](ukol-a.md) a [ukol-b.md](ukol-b.md).

## Cíl cvičení
Naučit se smysluplně zpřístupnit nový model v Django adminu a vytvořit realistická testovací data.

---

## Zadání

1. Zaregistrujte `Vypujcka` do `knihovna/admin.py`.
2. Vytvořte vlastní `ModelAdmin` pro `Vypujcka`:
   - `list_display`: `ctenar`, `kniha`, `stav`, `datum_vypujcky`, `termin_vraceni`
   - `list_filter`: `stav`, `datum_vypujcky`
   - `search_fields`: `ctenar`, `kniha__titul`
3. Proveďte migrace (pokud jsou nové změny modelu).
4. Vložte minimálně 8 testovacích záznamů:
   - alespoň 2 vrácené,
   - alespoň 2 po termínu,
   - různí čtenáři,
   - různé knihy.

---

## Povinné výstupy
- Upravený `knihovna/admin.py`.
- Screenshot seznamu výpůjček v adminu s aktivním filtrem.
- Výpis ze shellu potvrzující počet záznamů.

---

## Kontrolní kritéria
- [ ] model je v adminu viditelný,
- [ ] filtrování a vyhledávání funguje,
- [ ] data odpovídají scénářům ze zadání,
- [ ] admin je čitelný i při více záznamech.

---

## Nápověda
- Django admin: https://docs.djangoproject.com/en/6.0/ref/contrib/admin/
