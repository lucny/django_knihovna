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

---
### Vytvoření nového záznamu v databázi pomocí ORM v Django

Vytvoření nového záznamu v databázi pomocí ORM v Django je velmi jednoduché. 

- Nejprve musíme vytvořit novou instanci třídy, která reprezentuje tabulku v databázi. 
- Poté můžeme nastavit hodnoty atributů a uložit nový záznam do databáze pomocí metody `save()`.
 
Vytvoříme novou knihu a uložíme ji do databáze.

```bash
>>> nova_kniha = Kniha(titul='Nová kniha', rok_vydani=2023, pocet_stran=300, vydavatelstvi=Vydavatelstvi.objects.get(nazev='Host'))
>>> nova_kniha.save()
```

Vytvoříme nového autora a uložíme ho do databáze.

```bash
>>> novy_autor = Autor(jmeno='Jan', prijmeni='Novák', narozeni='1990-01-01')
>>> novy_autor.save()
```

Chceme-li obě operace provést najednou a zároveň vytvořit vazbu mezi knihou a autorem, můžeme použít metodu `create()`.

```bash
>>> nova_kniha = Kniha.objects.create(titul='Nová kniha', rok_vydani=2023, pocet_stran=300, vydavatelstvi=Vydavatelstvi.objects.get(nazev='Host'))
>>> novy_autor = Autor.objects.create(jmeno='Jan', prijmeni='Novák', narozeni='1990-01-01')
>>> nova_kniha.autori.add(novy_autor)
```

---
### Aktualizace záznamu v databázi pomocí ORM v Django

Aktualizace záznamu v databázi pomocí ORM v Django lze provést několika způsoby.
Ve všech případech musíme nejprve získat záznam, který chceme aktualizovat.

```bash
>>> kniha = Kniha.objects.get(id=1)
```

Poté můžeme změnit hodnoty atributů a uložit změny do databáze pomocí metody `save()`.

```bash
>>> kniha.titul = 'Nový název knihy'
>>> kniha.save()
```

Další možností je použití metody `update()`, která umožňuje aktualizovat záznamy v databázi pomocí filtru.

```bash
>>> Kniha.objects.filter(rok_vydani=2023).update(pocet_stran=400)
```

Metoda update_all() umožňuje aktualizovat všechny záznamy v dané tabulce.

```bash
>>> Kniha.objects.all().update(pocet_stran=500)
```

Metoda `update_or_create()` umožňuje aktualizovat existující záznam nebo vytvořit nový záznam, pokud neexistuje.

```bash
>>> nova_kniha, created = Kniha.objects.update_or_create(titul='Nová kniha', defaults={'rok_vydani': 2023, 'pocet_stran': 300, 'vydavatelstvi': Vydavatelstvi.objects.get(nazev='Host')})
```

V tomto příkladu se pokusíme aktualizovat záznam s názvem 'Nová kniha'. Pokud záznam neexistuje, vytvoří se nový záznam s danými hodnotami.

---
### Mazání záznamu z databáze pomocí ORM v Django

Mazání záznamu z databáze pomocí ORM v Django lze provést několika způsoby.
Nejprve musíme opět získat záznam, který chceme smazat.

```bash 
>>> kniha = Kniha.objects.get(id=1)
```

Poté můžeme záznam smazat pomocí metody `delete()`.

```bash
>>> kniha.delete()
```

Další možností je použití metody `filter()` a `delete()`, která umožňuje smazat záznamy v databázi pomocí filtru.

```bash
>>> Kniha.objects.filter(rok_vydani=2023).delete()
```

Metoda `delete_all()` umožňuje smazat všechny záznamy v dané tabulce.

```bash
>>> Kniha.objects.all().delete()
```

---
### Použití Q objektů v dotazech do databáze pomocí ORM v Django

Q objekty jsou objekty, které umožňují vytvářet složité dotazy do databáze pomocí logických operátorů AND, OR a NOT. 
Q objekty jsou tedy užitečné, pokud chceme vytvořit dotaz, obsahující více podmínek.

Příkladem může být dotaz, který vybere všechny knihy, které mají více než 300 stran **a** byly vydány po roce 2000.

```bash
>>> from django.db.models import Q
>>> knihy = Kniha.objects.filter(Q(pocet_stran__gt=300) & Q(rok_vydani__gt=2000))
```

Jiným příkladem může být dotaz, který vybere všechny knihy, které mají méně než 200 stran **nebo** byly vydány před rokem 2000.

```bash
>>> knihy = Kniha.objects.filter(Q(pocet_stran__lt=200) | Q(rok_vydani__lt=2000))
```

Operátor `~` umožňuje vytvořit negaci podmínky. 

```bash
>>> knihy = Kniha.objects.filter(~Q(pocet_stran__gt=300))
```

V tomto příkladu jsme vybrali všechny knihy, které mají méně než 300 stran, protože jsme použili negaci podmínky `pocet_stran__gt=300` (tj. počet stran není větší než 300).

---
### Použití F objektů v dotazech do databáze pomocí ORM v Django

F objekty jsou objekty, které umožňují vytvářet dotazy do databáze pomocí hodnot atributů v rámci jednoho záznamu.

Příkladem může být dotaz, který vybere všechny knihy, které mají více stran než je průměrný počet stran v databázi.

```bash
>>> from django.db.models import F
>>> prumerny_pocet_stran = Kniha.objects.aggregate(prumerny_pocet_stran=Avg('pocet_stran'))['prumerny_pocet_stran']
>>> knihy = Kniha.objects.filter(pocet_stran__gt=F('prumerny_pocet_stran'))
```

V tomto příkladu jsme nejprve získali průměrný počet stran v databázi pomocí metody `aggregate()`.
Poté jsme vybrali všechny knihy, které mají více stran než je průměrný počet stran v databázi pomocí F objektu.

Jiným příkladem může být dotaz, který zvýší počet stran všech knih o 100.

```bash
>>> Kniha.objects.all().update(pocet_stran=F('pocet_stran') + 100)
```

V tomto příkladu jsme použili metodu `update()` a F objekt, abychom zvýšili počet stran všech knih o 100.

---
### Použití Annotate objektů v dotazech do databáze pomocí ORM v Django

Annotate objekty jsou objekty, které umožňují vytvářet agregované dotazy do databáze pomocí funkcí jako je `Count()`, `Sum()`, `Avg()`, `Min()`, `Max()`.
Annotate objekty jsou užitečné, pokud chceme získat souhrnné informace o záznamech v databázi.

Příkladem může být dotaz, který vybere všechny žánry a zjistí počet knih v každém žánru.

```bash
>>> from django.db.models import Count
>>> zanry = Zanr.objects.annotate(pocet_knih=Count('kniha'))
```

V tomto příkladu jsme získali všechny žánry a zjistili počet knih v každém žánru pomocí metody `annotate()` a funkce `Count()`.
Výsledek je QuerySet, který obsahuje všechny žánry a počet knih v každém žánru.

Jiným příkladem může být dotaz, který vybere všechna vydavatelství a zjistí: 
- celkový počet knih vydávaných jednotlivými vydavatelstvími, 
- počet stran všech knih vydávaných jednotlivými vydavatelstvími,
- průměrný počet stran vydaných knih.

```bash
>>> from django.db.models import Sum, Avg
>>> vydavatelstvi = Vydavatelstvi.objects.annotate(pocet_knih=Count('kniha')).annotate(celkem_stran=Sum('kniha__pocet_stran')).annotate(prumer_stran=Avg('kniha__pocet_stran'))
```

Přehledný výpis výsledků pomocí cyklu `for`.
```bash
>>> for v in vydavatelstvi:                                      
...     print(v.nazev, v.pocet_knih, v.celkem_stran, v.prumer_stran)
... 
Bílá vrána 2 1008 504.0
Jota 2 792 396.0
Český spisovatel 2 586 293.0
Albatros 1 400 400.0
Host 5 1593 318.6
Jaroslav Jiránek 1 48 48.0
Odeon 1 304 304.0
Millenium Publishing 1 324 324.0
František Borový 1 122 122.0
Artur 1 102 102.0
Aventinum 2 297 148.5
Fortuna Libri 1 128 128.0
Svoboda 1 138 138.0
Mladá fronta 1 184 184.0
```

---
### Použití Aggregates objektů v dotazech do databáze pomocí ORM v Django

Aggregates objekty jsou objekty, které umožňují vytvářet agregované dotazy do databáze pomocí funkcí jako je `Count()`, `Sum()`, `Avg()`, `Min()`, `Max()`.
Aggregates objekty jsou užitečné, pokud chceme získat souhrnné informace o záznamech v databázi.

Rozdíl mezi Annotate a Aggregates objekty je ten, že Annotate objekty přidávají nové pole do QuerySetu, zatímco Aggregates objekty vrací jediný výsledek.

Příkladem může být dotaz, který zjistí celkový počet knih v databázi.

```bash
>>> from django.db.models import Count
>>> pocet_knih = Kniha.objects.aggregate(pocet_knih=Count('id'))['pocet_knih']
>>> pocet_knih
22
```

V tomto příkladu jsme získali celkový počet knih v databázi pomocí metody `aggregate()` a funkce `Count()`. 
Výsledek je slovník, který obsahuje celkový počet knih v databázi. Použili jsme proto klíč `pocet_knih`, abychom získali hodnotu.



Jiným příkladem může být dotaz, který zjistí celkový počet stran všech knih v databázi.

```bash
>>> celkem_stran = Kniha.objects.aggregate(celkem_stran=Sum('pocet_stran'))['celkem_stran']
>>> celkem_stran                                                                            
6026
```

---
### Použití Values objektů v dotazech do databáze pomocí ORM v Django

Values objekty jsou objekty, které umožňují vytvářet dotazy do databáze, které vracejí pouze určité hodnoty atributů záznamů.

Příkladem může být dotaz, který vybere pouze názvy knih a roky vydání.

```bash
>>> knihy = Kniha.objects.values('titul', 'rok_vydani')     
>>> knihy
<QuerySet [{'titul': 'Adam stvořitel', 'rok_vydani': 1929}, {'titul': 'Babička', 'rok_vydani': 2021}, {'titul': 'Bílá nemoc', 'rok_vydani': 1948}, {'titul': 'Divá Bára', 'rok_vydani': 1942}, {'titul': 'K moři', 'rok_vydani': 2007}, 
{'titul': 'Krakatit', 'rok_vydani': 2009}, {'titul': 'Královny nemají nohy', 'rok_vydani': 2000}, {'titul': 'Krásná čarodějka', 'rok_vydani': 1984}, {'titul': 'Markéta Lazarová', 'rok_vydani': 1980}, {'titul': 'Obsluhoval jsem angli
ckého krále', 'rok_vydani': 2007}, {'titul': 'Pekař Jan Marhoul', 'rok_vydani': 1972}, {'titul': 'Prsten Borgiů', 'rok_vydani': 2000}, {'titul': 'R.U.R.', 'rok_vydani': 2004}, {'titul': 'Rozmarné léto', 'rok_vydani': 2015}, {'titul'
: 'Tma', 'rok_vydani': 2007}, {'titul': 'Vitka', 'rok_vydani': 2018}, {'titul': 'Vyhnání Gerty Schnirch', 'rok_vydani': 2009}, {'titul': 'Zmizet', 'rok_vydani': 2009}, {'titul': 'Zářivé hlubiny', 'rok_vydani': 1924}, {'titul': 'Šikm
ý kostel', 'rok_vydani': 2020}, '...(remaining elements truncated)...']>
```

---
### Použití ValuesList objektů v dotazech do databáze pomocí ORM v Django

ValuesList objekty jsou objekty, které umožňují vytvářet dotazy do databáze, které vracejí pouze určité hodnoty atributů záznamů ve formě seznamu.

Příkladem může být dotaz, který vybere pouze názvy knih a roky vydání ve formě seznamu.

```bash
>>> knihy = Kniha.objects.values_list('titul', 'rok_vydani')
>>> knihy
<QuerySet [('Adam stvořitel', 1929), ('Babička', 2021), ('Bílá nemoc', 1948), ('Divá Bára', 1942), ('K moři', 2007), ('Krakatit', 2009), ('Královny nemají nohy', 2000), ('Krásná čarodějka', 1984), ('Markéta Lazarová', 1980), ('Obsluhoval
 jsem anglického krále', 2007), ('Pekař Jan Marhoul', 1972), ('Prsten Borgiů', 2000), ('R.U.R.', 2004), ('Rozmarné léto', 2015), ('Tma', 2007), ('Vitka', 2018), ('Vyhnání Gerty Schnirch', 2009), ('Zmizet', 2009), ('Zářivé hlubiny', 1924),
 ('Šikmý kostel', 2020), '...(remaining elements truncated)...']>
```

---
## Využití ORM v Django ve skriptech

### Automatické vytváření záznamů z CSV souboru

ORM v Django můžeme využít i ve skriptech, pomocí nichž můžeme provádět různé operace s databází mimo běžící Django aplikaci.

Příkladem může být skript, který vytváří nové záznamy uživatelů v databázi na základě dat z CSV souboru.

Nejprve si připravíme CSV soubor `uzivatele.csv` s následujícím obsahem:

```csv
uzivatel;heslo;jmeno;prijmeni;email
martinholy;student;Martin;Holý;martin.holy@student.cz
janachytra;student;Jana;Chytrá;jana.chytra@student.cz
...
```

Poté vytvoříme nový skript `import_users.py` v adresáři `knihovna/management/commands/`. 

>[!NOTE]
> Tato cesta je standardní pro vlastní management příkazy v Django. 
> Pomocí management příkazů můžeme vytvářet vlastní skripty, které můžeme spouštět pomocí `python manage.py`.
> 
> Vytvoření nového management příkazu je velmi jednoduché. 
> Vyžaduje pouze vytvoření nové třídy odvozené od `BaseCommand` a implementaci metody `handle()`.
> Součástí třídy je atribut `help`, který obsahuje nápovědu k příkazu.
> Metoda `handle()` obsahuje kód, který se spustí při spuštění příkazu.
> 
> Více informací o management příkazech naleznete v oficiální dokumentaci Django: [https://docs.djangoproject.com/en/5.0/howto/custom-management-commands/](https://docs.djangoproject.com/en/3.2/howto/custom-management-commands/).

```python
import csv
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Imports users from a CSV file'

    def handle(self, *args, **kwargs):
        # Cesta k souboru CSV
        file_path = 'knihovna/management/data/uzivatele.csv'

        # Načtení a zpracování CSV souboru
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                username, password, first_name, last_name, email = row
                if not User.objects.filter(username=username).exists():
                    User.objects.create_user(username=username, password=password, first_name=first_name,
                                             last_name=last_name, email=email)
                    print(f'Uživatel {username} byl úspěšně přidán.')
                else:
                    print(f'Uživatel {username} již existuje.')
```

> [!NOTE]
> Skript načte data z CSV souboru a vytvoří nové uživatele v databázi pomocí metody `create_user()`.
> Pro kontrolu, zda uživatel již existuje, jsme použili metodu `exists()`.
> Nakonec jsme vytvořili nový záznam uživatele v databázi a vypsali informaci o úspěšném přidání.

Skript můžeme spustit pomocí příkazu `python manage.py import_users`.

```bash
❯ py .\manage.py import_users
Uživatel martinholy byl úspěšně přidán.
Uživatel janachytra byl úspěšně přidán.
...
```

Výsledkem spuštění skriptu je automatické vytvoření nových uživatelů v databázi na základě dat z CSV souboru.

### Vytváření fake dat pomocí knihovny Faker

ORM v Django můžeme využít ve skriptech, pomocí nichž můžeme generovat *fake data* a vytvářet nové záznamy v databázi.
**Fake data** jsou náhodná data, která mohou být použita pro testování a vývoj aplikací.

Knihovna **Faker** je nástroj, který umožňuje generovat fake data.

>[!NOTE]
> **Faker** je knihovna pro generování fake dat v Pythonu.
> Faker podporuje mnoho jazyků a formátů, jako jsou jména, adresy, e-maily, texty, čísla, atd.
> Bližší informace o knihovně Faker naleznete na stránkách [https://faker.readthedocs.io/en/master/](https://faker.readthedocs.io/en/master/).

Příkladem může být skript, který vytváří nové záznamy recenzí.

Nejprve nainstalujeme knihovnu Faker pomocí příkazu `pip install faker`.

Poté vytvoříme nový skript `generate_reviews.py` v adresáři `knihovna/management/commands/`.

```python
import random
from faker import Faker
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from knihovna.models import Kniha, Recenze

class Command(BaseCommand):
    help = 'Generates fake reviews for books'

    def handle(self, *args, **kwargs):
        fake = Faker('cs_CZ')  # Pro generování v češtině
        users = User.objects.filter(id__range=(3, 12))  # Uživatelé s ID 3 až 12
        books = Kniha.objects.filter(id__range=(1, 22))  # Knihy s ID 1 až 22

        for _ in range(100):
            book = random.choice(books)
            user = random.choice(users)
            # Kontrola, zda už uživatel nenapsal recenzi na danou knihu
            if not Recenze.objects.filter(kniha=book, recenzent=user).exists():
                Recenze.objects.create(
                    text=fake.text(),
                    kniha=book,
                    recenzent=user,
                    hodnoceni=random.randint(1, 5)
                )
            else:
                print(f'Uživatel {user} již napsal recenzi na knihu {book}. Přeskakuji.')

        print('Recenze byly úspěšně vygenerovány.')
```

> [!NOTE]
> Skript generuje fake recenze pro knihy a ukládá je do databáze.
> Pro generování fake dat jsme použili knihovnu `Faker` a metody pro generování náhodných textů, čísel a hodnocení.
> Pro kontrolu, zda už uživatel nenapsal recenzi na danou knihu, jsme použili metodu `exists()`.
> Nakonec jsme vytvořili nový záznam recenze v databázi pomocí metody `create()`.


Skript můžeme spustit pomocí příkazu `python manage.py generate_reviews`.

```bash
❯ py .\manage.py generate_reviews
Recenze byly úspěšně vygenerovány.
```

### Aktualizace záznamů v databázi pomocí skriptu

Dalším příkladem může být skript, který hromadně aktualizuje záznamy v databázi.

Příkladem může být skript `update_review_dates.py`, který aktualizuje datum vytvoření recenzí tak,
aby bylo nastaveno na náhodné datum i náhodný čas v rozmezí určitého období.

```python
from datetime import datetime, timedelta
import random
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware
from knihovna.models import Recenze

class Command(BaseCommand):
    help = 'Updates the "upraveno" field of reviews with random dates and times'

    def handle(self, *args, **kwargs):
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 3, 20)
        delta = end_date - start_date

        recenze_qs = Recenze.objects.all()

        for recenze in recenze_qs:
            random_number_of_days = random.randrange(delta.days)
            random_date = start_date + timedelta(days=random_number_of_days)
            random_time = (datetime.min + timedelta(seconds=random.randint(0, 86399))).time()
            random_datetime = datetime.combine(random_date, random_time)
            recenze.upraveno = make_aware(random_datetime)
            recenze.save()

        print(f'Časové údaje "upraveno" byly úspěšně aktualizovány pro {recenze_qs.count()} recenzí.')
```

> [!NOTE]
> Skript aktualizuje datum vytvoření recenzí na náhodné datum i náhodný čas v rozmezí zadaného období.
> Pro generování náhodného data a času jsme použili knihovnu `random` a metodu `randrange()` pro náhodný počet dní a metodu `randint()` pro náhodný čas.
> Pro konverzi náhodného data a času na `datetime` objekt jsme použili metodu `combine()` a metodu `make_aware()` pro nastavení časové zóny.
> Nakonec jsme uložili změny do databáze pomocí metody `save()`.

Skript můžeme spustit pomocí příkazu `python manage.py update_review_dates`.

```bash
❯ py .\manage.py update_review_dates
Časové údaje "upraveno" byly úspěšně aktualizovány pro 86 recenzí.
```

---
## Cvičné otázky a úkoly

1. Co je ORM a jaký je jeho účel?
2. Jaký je rozdíl mezi ORM a SQL?
3. Jaký je rozdíl mezi QuerySet a SQL dotazem?

### Praktické úkoly: Vytváření nových záznamů v databázi pomocí ORM v Django

1. Vytvořte pomocí ORM v Django nový záznam v tabulce `Autor`.
2. Vytvořte pomocí ORM v Django nový záznam v tabulce `Kniha`, který bude mít vazbu na záznam autora z předchozího úkolu.
Zajistěte rovněž vytvoření vazby mezi knihou a vydavatelstvím, podobně i vazbu mezi knihou a žánry. Pokud žánr nebo vydavatelství neexistuje, vytvořte je.

### Praktické úkoly: Aktualizace záznamu v databázi pomocí ORM v Django
1. Aktualizujte pomocí ORM v Django záznam autora z předchozího úkolu vložením věty do jeho biografie.
2. Aktualizujte pomocí ORM v Django záznam knihy z předchozího úkolu změnou počtu stran na 400 a roku vydání na 2022.

### Praktické úkoly: Mazání záznamu z databáze pomocí ORM v Django
1. Smažte pomocí ORM v Django záznam knihy z předchozích úkolů.
2. Smažte pomocí ORM v Django záznam autora z předchozích úkolů.

### Praktické úkoly: Výběr záznamů z databáze pomocí ORM v Django
1. Vypište pomocí ORM všechny záznamy z tabulky `Kniha`, které mají méně než 200 stran. Seřaďte výsledky podle počtu stran vzestupně.

```bash
>>> 
```

2. Vypište pomocí ORM všechny záznamy z tabulky `Kniha`, které byly vydány po roce 2000 a patří do žánru "román". Seřaďte výsledky podle roku vydání sestupně.

```bash
>>> 
```

3. Vypište pomocí ORM všechny autory, jejichž jméno začíná na písmeno "B" a příjmení na "V". Seřaďte výsledky podle příjmení vzestupně.

```bash
>>> 
```

4. Vypište pomocí ORM všechny recenze, které byly vytvořeny v únoru 2024, vyjma těch, které byly napsány uživateli, 
jejichž email obsahuje doménu "ucitel.cz". Zobrazeny budou sloupce `id`, `text`, `upraveno`, `email recenzenta` a `název knihy`.
Zobrazení výsledků seřaďte od nejnovějších recenzí a omezte na prvních **5 záznamů**.   

```bash
>>> 
```
5. Vypište pomocí ORM počty recenzí seskupené podle recenzentů. Výsledky zobrazte ve formátu `recenzent` (id, příjmení, jméno) a `pocet_recenzi`. 
Seřaďte výsledky podle počtu recenzí sestupně, sekundárně podle příjmení recenzenta vzestupně.

```bash
>>> 
```

6. Vypište pomocí ORM průměrné hodnocení všech knih, které byly vydány před rokem 2000.

```bash
>>> 
```
   
7. Vypište pomocí ORM součty stran všech knih a počet knih v databázi, na kterých se podíleli bratři Čapkové.

```bash
>>> 
```
8. Vypište pomocí ORM sestavu, která bude obsahovat sloupce: název knihy, nejvyšší hodnocení, nejnižší hodnocení, datum poslední recenze.

```bash
>>> 
```






