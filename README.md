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

**Řešení:**

V souboru `models.py` vytvořte nový model `Recenze`:

```python
# Import třídy User z balíčku django.contrib.auth.models
from django.contrib.auth.models import User
...
# Vytvoření modelu Recenze
class Recenze(models.Model):
    text = models.TextField(verbose_name='Text recenze', help_text='Vložte text recenze')
    kniha = models.ForeignKey(Kniha, on_delete=models.RESTRICT, verbose_name='Kniha')
    recenzent = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Recenzent')
    HODNOCENI_KNIHY = (
        (0, ''),
        (1, '*'),
        (2, '**'),
        (3, '***'),
        (4, '****'),
        (5, '*****'),
    )
    hodnoceni = models.PositiveSmallIntegerField(verbose_name='Hodnocení', default=3, choices=HODNOCENI_KNIHY)
    upraveno = models.DateTimeField(auto_now=True)
```

**Poznámky k řešení:**

Třída `Recenze` dědí od třídy `models.Model`, která je součástí balíčku `django.db.models`. Tento balíček obsahuje
třídy a funkce, které umožňují definovat strukturu databáze.

Podrobnější informace o tvorbě modelů naleznete v oficiální dokumentaci Django:

- [Django - Modely](https://docs.djangoproject.com/en/5.0/topics/db/models/)

Modelové třídy obsahují atributy, které reprezentují jednotlivé sloupce v databázové tabulce.
Pro každý sloupec je definován typ pole a další parametry, které ovlivňují jeho chování.

Podrobnější informace o jednotlivých typech polí naleznete v oficiální dokumentaci Django:

- [Django - Pole modelů](https://docs.djangoproject.com/en/5.0/topics/db/models/#fields)
  Podrobnější informace o jednotlivých parametrech polí naleznete v oficiální dokumentaci Django:
- [Django - Parametry polí](https://docs.djangoproject.com/en/5.0/ref/models/fields/#field-options)

Součástí modelu `Recenze` jsou následující pole:

- Pole `text` je typu `TextField` (
  viz [Django - TextField](https://docs.djangoproject.com/en/5.0/ref/models/fields/#textfield)),
  který umožňuje ukládat textové řetězce libovolné délky.
    - Parametr `verbose_name` (
      viz [Django - verbose_name](https://docs.djangoproject.com/en/5.0/ref/models/fields/#verbose-name))
      slouží k definici popisku sloupce v administraci.
    - Parametr `help_text` (viz [Django - help_text](https://docs.djangoproject.com/en/5.0/ref/models/fields/#help-text)
      slouží k definici návodného textu pro zadávající uživatele.
- Pole `kniha` je cizím klíčem na model `Kniha` (
  viz [Django - ForeignKey](https://docs.djangoproject.com/en/5.0/ref/models/fields/#foreignkey)),
  který umožňuje provázat recenzi s konkrétní knihou.
    - Parametr `on_delete` (
      viz [Django - on_delete](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.ForeignKey.on_delete))
      určuje chování databáze při smazání propojeného záznamu. Konkrétně nastavení `models.RESTRICT` znamená, že v
      případě pokusu o smazání knihy bude smazání zablokováno, protože na ni existuje odkaz v tabulce recenzí.
    - Parametr `verbose_name` slouží k definici popisku sloupce v administraci.
- Pole `recenzent` je cizím klíčem na model `User`, který umožňuje provázat recenzi s konkrétním uživatelem.
  Model `User` je součástí balíčku `django.contrib.auth.models` (ten je třeba správně importovat) a obsahuje informace o
  uživatelích aplikace (
  viz [Django - User](https://docs.djangoproject.com/en/5.0/ref/contrib/auth/#django.contrib.auth.models.User)).
    - Parametr `on_delete` určuje chování databáze při smazání propojeného záznamu. Konkrétně nastavení `models.CASCADE`
      znamená, že v případě smazání uživatele budou smazány i všechny jeho recenze.
    - Parametr `verbose_name` slouží k definici popisku sloupce v administraci.
- Pole `hodnoceni` je typu `PositiveSmallIntegerField` (je určeno pro ukládání celých čísel v rozsahu 0 až 32767).
    - Kromě základního parametru `verbose_name` je definován parametr `choices` (
      viz [Django - choices](https://docs.djangoproject.com/en/5.0/ref/models/fields/#choices)), který umožňuje výběr z
      předem definovaných hodnot připravených v konstantě `HODNOCENI_KNIHY`. Každá hodnota seznamu (list) je dvojice (
      n-tice) obsahující číselnou hodnotu a textový popis.
    - Výchozí hodnota je atributem `default` nastavena na 3.
- Pole `upraveno` je typu `DateTimeField` (
  viz [Django - DateTimeField](https://docs.djangoproject.com/en/5.0/ref/models/fields/#datetimefield)),
  který umožňuje ukládat datum a čas poslední úpravy záznamu.
    - Parametr `auto_now` (
      viz [Django - auto_now](https://docs.djangoproject.com/en/5.0/ref/models/fields/#django.db.models.DateField))
      je nastaven na `True`, což znamená, že se do tohoto pole automaticky uloží aktuální datum a čas při každé
      aktualizaci záznamu.

Aby se model `Recenze` objevil také v databázi, je třeba provést migraci, která vytvoří odpovídající tabulku.
Migraci provedeme pomocí příkazů `python manage.py makemigrations` a `python manage.py migrate`.
Výsledek migrace můžeme zkontrolovat v PyCharmu v záložce `Database`:

![Databázová tabulka Recenze](./docs/img/db-knihovna_recenze.png)