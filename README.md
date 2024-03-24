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
## ORM - Objektově relační mapování

ORM je způsob, jakým se v Django pracuje s databází. 
Vytváříme třídy, které se následně mapují na tabulky v databázi. 
ORM nám umožňuje pracovat s databází pomocí objektů a metod, které jsou vytvořeny v třídách.

>[!IMPORTANT]
> #### Jak ORM funguje?
> ORM vytváří třídy, které se mapují na tabulky v databázi. Třídy obsahují atributy, které se mapují na sloupce v tabulce. ORM nám umožňuje pracovat s databází pomocí objektů a metod, které jsou vytvořeny v třídách.
> 
> #### Výhody ORM
> - Snadná práce s databází
> - Snadná údržba kódu
> - Bezpečnost
> - Snadná migrace
> - Snadná integrace s ostatními systémy a programovacími jazyky
> 
> #### Nevýhody ORM
> - Pomalejší načítání dat
> - Složitější optimalizace
> - Složitější ladění
> 
> #### ORM v Django
> Django používá ORM, které je založeno na knihovně `django.db.models`. ORM v Django je velmi výkonné a umožňuje nám pracovat s databází pomocí objektů a metod, které jsou vytvořeny v třídách.

### Zadávání dotazů do databáze pomocí ORM v Django

Pro otestování ORM v Django můžeme použít **Django shell**. 

**Django shell** je interaktivní konzole, která nám umožňuje pracovat s Django aplikací a databází.

Django shell spustíme pomocí příkazu `python manage.py shell`.

```bash
❯ py manage.py shell
Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> 
```

Nejprve musíme importovat modely, se kterými chceme pracovat.

```bash
>>> from knihovna.models import Kniha, Autor, Zanr, Vydavatelstvi
```

Potom můžeme zadávat dotazy do databáze pomocí ORM.

```bash
>>> Kniha.objects.all()
<QuerySet [<Kniha: Adam stvořitel (1929)>, <Kniha: Babička (2021)>, <Kniha: Bílá nemoc (1948)>, <Kniha: Divá Bára (1942)>, <Kniha: K moři (2007)>, <Kniha: Krakatit (2009)>, <Kniha: Královny nemají nohy (2000)>, <Kniha: Krásná čarodě
jka (1984)>, <Kniha: Markéta Lazarová (1980)>, <Kniha: Obsluhoval jsem anglického krále (2007)>, <Kniha: Pekař Jan Marhoul (1972)>, <Kniha: Prsten Borgiů (2000)>, <Kniha: R.U.R. (2004)>, <Kniha: Rozmarné léto (2015)>, <Kniha: Tma (2
007)>, <Kniha: Vitka (2018)>, <Kniha: Vyhnání Gerty Schnirch (2009)>, <Kniha: Zmizet (2009)>, <Kniha: Zářivé hlubiny (1924)>, <Kniha: Šikmý kostel (2020)>, '...(remaining elements truncated)...']>
>>>
```
V tomto příkladu jsme získali všechny knihy z databáze.

### Příklady dotazů do databáze pomocí ORM v Django

Všechny knihy
```bash
>>> knihy = Kniha.objects.all()
```

Jedna kniha
```bash
>>> kniha = knihy.get(id=10)
```

Všichni autoři dané knihy
```bash
>>> kniha.autori.all()
<QuerySet [<Autor: Kateřina Tučková>]>
```

Všechny žánry dané knihy
```bash
>>> kniha.zanry.all()
<QuerySet [<Zanr: psychologický>, <Zanr: román>, <Zanr: společenský>]>
```

Jeden autor
```bash
autor = Autor.objects.get(id=1)
```

Všechny knihy daného autora
```bash
>>> autor.kniha_set.all()
<QuerySet [<Kniha: Šikmý kostel (2020)>, <Kniha: Šikmý kostel 2 (2021)>]>
```

První z knih daného autora
```bash
>>> autor.kniha_set.all()[0].titul 
'Šikmý kostel'
```

Všechny žánry této knihy
```bash
>>> autor.kniha_set.all()[0].zanry.all()
<QuerySet [<Zanr: historický>, <Zanr: román>]>
```

Název vydavatelství této knihy
```bash
>>> autor.kniha_set.all()[0].vydavatelstvi.nazev
'Bílá vrána'
```

Vyber žánr 'román'
```bash
>>> zanr = Zanr.objects.filter(nazev__exact = 'román')
```

Vyber žánr s id 1
```bash
>>> z = Zanr.objects.get(id=1) 
```

Všechny knihy v daném žánru
```bash
>>> z.kniha_set.all()
<QuerySet [<Kniha: Babička (2021)>, <Kniha: K moři (2007)>, <Kniha: Krakatit (2009)>, <Kniha: Královny nemají nohy (2000)>, <Kniha: Krásná čarodějka (1984)>, <Kniha: Markéta Lazarová (1980)>, <Kniha: Obsluhoval jsem anglického krále
 (2007)>, <Kniha: Pekař Jan Marhoul (1972)>, <Kniha: Prsten Borgiů (2000)>, <Kniha: Rozmarné léto (2015)>, <Kniha: Tma (2007)>, <Kniha: Vyhnání Gerty Schnirch (2009)>, <Kniha: Šikmý kostel (2020)>, <Kniha: Šikmý kostel 2 (2021)>, <K
niha: Žítkovské bohyně (2012)>]>

```

Všechny žánry, které mají v názvu 'n' a nemají v názvu 'm' a jsou seřazeny sestupně
```bash
>>> z = Zanr.objects.filter(nazev__contains = 'n').exclude(nazev__contains = 'm').order_by('-nazev')
>>> z
<QuerySet [<Zanr: životopisný>, <Zanr: společenský>, <Zanr: dobrodružný>]>
```

Počet knih v knihovně
```bash
>>> knihy.count()
22
```

Počet knih historického a humoristického žánru
```bash
>>> from django.db.models import Q
>>> knihy.filter(Q(zanry__nazev__contains = 'humor') | Q(zanry__nazev__contains = 'histor')).count()
10
```

První a poslední kniha v databázi
```bash
>>> knihy.first()
<Kniha: Adam stvořitel (1929)>
>>> knihy.last()
<Kniha: Žítkovské bohyně (2012)>
```

Autoři narození v rozmezí let 1900 - 1950
```bash
>>> import datetime
>>> start_date = datetime.date(1900, 1, 1)
>>> end_date = datetime.date(1950, 12, 31)
>>> Autor.objects.filter(narozeni__gte = start_date).filter(narozeni__lte = end_date)
<QuerySet [<Autor: Bohumil Hrabal>, <Autor: Ondřej Neff>, <Autor: Vladimír Neff>]>
```

Průměrný rok vydání knihy
```bash
>>> from django.db.models import Avg
>>> knihy.aggregate(prum_rok_vydani=Avg('rok_vydani'))
{'prum_rok_vydani': 1992.6363636363637}
```

Vypište souhrnné údaje o žánrech - název žánru, počet knih daného žánru, celkový a průměrný počet stran, rok vydání nejstarší knihy v daném žánru
Seřaďte dynamickou sadu primárně podle počtu knih (sestupně) a sekundárně podle roku vydání nejstarší knihy (vzestupně).
```bash
>>> from django.db.models import Count, Avg, Min, Sum
>>> knihy.values('zanry__nazev').annotate(pocet_knih=Count('id')).annotate(prumer_stran=Avg('pocet_stran')).annotate(nejstarsi=Min('rok_vydani')).annotate(celkem_stran=Sum('pocet_stran')).order_by('-pocet_knih', 'nejstarsi')
<QuerySet [{'zanry__nazev': 'román', 'pocet_knih': 15, 'prumer_stran': 329.1333333333333, 'nejstarsi': 1972, 'celkem_stran': 4937}, {'zanry__nazev': 'historický', 'pocet_knih': 8, 'prumer_stran': 371.875, 'nejstarsi': 1980, 'celkem_
stran': 2975}, {'zanry__nazev': 'psychologický', 'pocet_knih': 5, 'prumer_stran': 324.4, 'nejstarsi': 1924, 'celkem_stran': 1622}, {'zanry__nazev': 'sci-fi', 'pocet_knih': 5, 'prumer_stran': 208.0, 'nejstarsi': 1929, 'celkem_stran':
 1040}, {'zanry__nazev': 'společenský', 'pocet_knih': 5, 'prumer_stran': 226.0, 'nejstarsi': 1942, 'celkem_stran': 1130}, {'zanry__nazev': 'drama', 'pocet_knih': 4, 'prumer_stran': 123.0, 'nejstarsi': 1929, 'celkem_stran': 492}, {'z
anry__nazev': 'povídky', 'pocet_knih': 3, 'prumer_stran': 199.0, 'nejstarsi': 1924, 'celkem_stran': 597}, {'zanry__nazev': 'humoristický', 'pocet_knih': 2, 'prumer_stran': 156.0, 'nejstarsi': 2007, 'celkem_stran': 312}, {'zanry__naz
ev': 'utopie', 'pocet_knih': 1, 'prumer_stran': 102.0, 'nejstarsi': 2004, 'celkem_stran': 102}, {'zanry__nazev': 'dobrodružný', 'pocet_knih': 1, 'prumer_stran': 324.0, 'nejstarsi': 2009, 'celkem_stran': 324}, {'zanry__nazev': 'život
opisný', 'pocet_knih': 1, 'prumer_stran': 176.0, 'nejstarsi': 2018, 'celkem_stran': 176}]>
```
Vypište souhrnné údaje o vydavatelství - název vydavatelství, počet vydaných knih, celkový počet stran
Vyberte pouze vydavatelství, která vydala dvě a více knih nebo vydavatelství s počtem vydaných stran nižším než 100.
Seřaďte dynamickou sadu primárně podle počtu knih (sestupně) a sekundárně podle počtu stran (vzestupně).
```bash
>>> knihy.values('vydavatelstvi__nazev').annotate(pocet_knih = Count('id')).annotate(celkem_stran = Sum('pocet_stran')).filter(Q(pocet_knih__gte = 2)|Q(celkem_stran__lt = 100)).order_by('-pocet_knih', 'celkem_stran')
<QuerySet [{'vydavatelstvi__nazev': 'Host', 'pocet_knih': 5, 'celkem_stran': 1593}, {'vydavatelstvi__nazev': 'Aventinum', 'pocet_knih': 2, 'celkem_stran': 297}, {'vydavatelstvi__nazev': 'Český spisovatel', 'pocet_knih': 2, 'celkem_s
tran': 586}, {'vydavatelstvi__nazev': 'Jota', 'pocet_knih': 2, 'celkem_stran': 792}, {'vydavatelstvi__nazev': 'Bílá vrána', 'pocet_knih': 2, 'celkem_stran': 1008}, {'vydavatelstvi__nazev': 'Jaroslav Jiránek', 'pocet_knih': 1, 'celke
m_stran': 48}]>
```