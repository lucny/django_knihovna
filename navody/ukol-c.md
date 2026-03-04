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
   - `search_fields`: `ctenar__username`, `ctenar__first_name`, `ctenar__last_name`, `kniha__titul`
3. V admin formuláři povolte ve výběru `ctenar` jen uživatele ze skupiny `readers`.
4. Proveďte migrace (pokud jsou nové změny modelu).
5. Vložte minimálně 8 testovacích záznamů:
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
- [ ] ve formuláři výpůjčky jsou nabídnuti pouze uživatelé ze skupiny `readers`,
- [ ] data odpovídají scénářům ze zadání,
- [ ] admin je čitelný i při více záznamech.


---

## Nápověda
- Django admin: https://docs.djangoproject.com/en/6.0/ref/contrib/admin/
