# Cvičný úkol G — mapování URL pro výpůjčky a čtenáře

## Návaznost
Navazuje na [ukol-d.md](ukol-d.md), [ukol-e.md](ukol-e.md), [ukol-f.md](ukol-f.md).

## Cíl cvičení
Udržet URL architekturu konzistentní a čitelnou.

---

## Zadání
V `knihovna/urls.py` vytvořte a pojmenujte všechny cesty:

- `loans/` (seznam výpůjček)
- `loans/<int:pk>/` (detail výpůjčky)
- `readers/` (seznam čtenářů)
- `readers/<slug:reader_slug>/` (detail čtenáře)

V `mat_knihovna/urls.py` zachovejte připojení aplikace pod `/knihovna/`.

Požadavky:
1. V šablonách nepoužívejte natvrdo cesty, pouze `{% url %}`.
2. Zkontrolujte, že navigace obsahuje odkazy na knihy, autory i výpůjčky.

---

## Povinné výstupy
- Upravené `knihovna/urls.py` a případně `mat_knihovna/urls.py`.
- Funkční navigace mezi všemi relevantními stránkami.

---

## Kontrolní kritéria
- [ ] žádný `NoReverseMatch`,
- [ ] žádné nefunkční odkazy v navbaru,
- [ ] URL názvy jsou jednoznačné a srozumitelné,
- [ ] detail čtenáře funguje i pro jména s mezerou/diakritikou (pokud je řešíte přes slug).

---

## Nápověda
- URL dispatcher: https://docs.djangoproject.com/en/6.0/topics/http/urls/
