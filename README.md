# Django - Školní knihovna
## Školní příklad
### Instalace
1. Klonování repozitáře
- `git clone https://github.com/lucny/django_knihovna.git`
2. Přesun do adresáře webu
- `python -m venv .venv`
3. Vytvoření virtuálního prostředí do složky .venv
- `python -m venv .venv`
4. Aktivace virtuálního prostředí 
- `.venv\Scripts\activate` (aktivace virtuálního prostředí - ve Windows)
- `.venv/bin/activate` (aktivace virtuálního prostředí - v Linuxu)
5. Instalace závislostí
- `pip install -r requirements.txt`
6. Spuštění aplikace
- `python manage.py runserver`

### Přístupové údaje do administrace
- superuživatel: `admin`
- heslo: `admin`

---
## Řešení praktických úloh

### 1. Vytvoření nového modelu Rezervace

**Zadání:** 

- V souboru `models.py` vytvořte nový model **Recenze**, který umožní *oprávněným uživatelům* přidávat do
aplikace recenze vybrané knihy (obě pole - `recenzent` a `kniha` - budou provázána s už existujícími modely
vztahy 1:N). 
- Součástí recenze bude *povinné* textové pole `text` (bude sloužit k zapsání textu recenze) a
*povinný* výběrový seznam `hodnoceni` (umožňuje zadat hodnocení v rozsahu *0 až 5*, přičemž do databáze se
uloží číselná hodnota a v seznamu uživatel uvidí řetězec tvořený příslušným *počtem hvězdiček*; výchozí
hodnota bude nastavena na *3*). 
- Součástí modelu bude také pole `upraveno`, jehož prostřednictvím bude v databázi automaticky uloženo datum, 
kdy byla recenze naposledy *aktualizována*. 
- Nezapomeňte v modelu nastavit vhodná pojmenování *popisků jednotlivých polí*, připojit stručné *návodné
texty* pro zadávající uživatele a možná *chybová hlášení*.

**Příloha:**

![Zaznam recenze v administraci](./docs/img/recenze-zaznam.png)


