# Cvičný úkol J — finální integrační kontrola modulu výpůjček

## Návaznost
Závěrečný úkol navazuje na [ukol-a.md](ukol-a.md) až [ukol-i.md](ukol-i.md).

## Cíl cvičení
Naučit studenta dělat „release check“: funkční, datová i prezentační kontrola před odevzdáním.

---

## Zadání
Proveďte kompletní kontrolu implementace modulu výpůjček:

1. Spusťte technické kontroly:
   - `python manage.py check`
   - `python manage.py makemigrations --check`
2. Ověřte klíčové URL:
   - seznam výpůjček,
   - detail výpůjčky,
   - seznam čtenářů,
   - detail čtenáře.
3. Ověřte chybové scénáře:
   - neexistující ID výpůjčky,
   - neexistující čtenář,
   - neplatné URL.
4. Ověřte kvalitu HTML a přístupnost:
   - validní struktura,
   - `alt` u obrázků,
   - popisné odkazy.
5. Ověřte datovou konzistenci:
   - stavy výpůjček dávají smysl,
   - termíny vrácení nejsou před datem výpůjčky,
   - po termínu jsou správně označené.

---

## Povinné výstupy
- Krátký kontrolní protokol (např. `navody/protokol-vypujcky.md`) se sekcemi:
  - Co bylo testováno
  - Co prošlo
  - Co bylo opraveno
  - Co zůstává k dopracování

---

## Kontrolní kritéria
- [ ] projekt prochází technické kontroly,
- [ ] všechny nové stránky fungují,
- [ ] chybové scénáře jsou ošetřené,
- [ ] výstup je připravený k odevzdání.

---

## Nápověda
- Deployment checklist (inspirace): https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/
