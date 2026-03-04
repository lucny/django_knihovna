# Návod A — vytvoření modelu `Recenze` opravdu krok za krokem

## Než začneš

1. Otevři terminál v kořeni projektu (`D:\django_knihovna`).
2. Aktivuj virtuální prostředí:
	- Windows PowerShell: `D:\django_knihovna\.venv\Scripts\Activate.ps1`
3. Ověř, že projekt běží:
	- `python manage.py runserver`
4. Pro rychlé testy modelů používej shell:
	- `python manage.py shell`
5. Když narazíš na chybu, začni kontrolou:
	- `python manage.py check`

---

## Cíl úlohy
Vytvořit v `knihovna/models.py` nový Django model `Recenze` tak, aby přesně splňoval zadání:
- vazba 1:N na recenzenta,
- vazba 1:N na knihu,
- povinný text recenze,
- povinné hodnocení 0–5 formou výběru,
- automatické ukládání času poslední změny.

### Co je důležité pochopit před začátkem
- Každý model v Djangu je **Python třída**.
- Třída modelu **dědí z `models.Model`**, tím Djangu říkáte: „toto je databázová tabulka“.
- Každý atribut třídy typu `models.*Field(...)` je sloupec v databázi.

Oficiální dokumentace:
- Modely: https://docs.djangoproject.com/en/6.0/topics/db/models/
- Pole modelů: https://docs.djangoproject.com/en/6.0/ref/models/fields/

---

## Postup krok za krokem

---

## Krok 1: Vytvořte prázdnou třídu modelu

### Kód pro tento krok
Do `knihovna/models.py` na konec souboru vložte:

```python
class Recenze(models.Model):
	pass
```

### Vysvětlení
- `class Recenze(...)`: vytváří novou třídu s názvem `Recenze`.
- `models.Model`: základní třída Django ORM.
- `pass`: dočasný obsah, dokud nepřidáte pole.

### Ověření kroku
Soubor se uloží bez chyby a editor nehlásí syntaktickou chybu.

---

## Krok 2: Přidejte volby hodnocení (`choices`)

### Kód pro tento krok
Nahradíte `pass` touto konstantou:

```python
class Recenze(models.Model):
	HODNOCENI_CHOICES = (
		(0, '☆☆☆☆☆'),
		(1, '★☆☆☆☆'),
		(2, '★★☆☆☆'),
		(3, '★★★☆☆'),
		(4, '★★★★☆'),
		(5, '★★★★★'),
	)
```

### Vysvětlení
- `HODNOCENI_CHOICES`: konvence je psát konstanty velkými písmeny.
- Každá položka je dvojice `(hodnota_do_DB, text_pro_formulář)`.
- Díky tomu se do databáze ukládá číslo, ale uživatel vidí hvězdičky.

### Ověření kroku
Konstanta je uvnitř třídy `Recenze` (odsazení 4 mezery).

Dokumentace k `choices`:
https://docs.djangoproject.com/en/6.0/ref/models/fields/#choices

---

## Krok 3: Přidejte vazbu na recenzenta (`ForeignKey`)

### Kód pro tento krok
Do třídy pod konstantu přidejte:

```python
recenzent = models.ForeignKey(
	Autor,
	on_delete=models.CASCADE,
	verbose_name='Recenzent',
	help_text='Vyberte autora recenze',
	error_messages={'null': 'Recenzent musí být vybrán'}
)
```

### Vysvětlení
- `ForeignKey(Autor, ...)`: jeden autor může mít více recenzí (1:N).
- `on_delete=models.CASCADE`: při smazání autora smaž i související recenze.
- `verbose_name`: text popisku v administraci/formulářích.
- `help_text`: nápověda pod polem.
- `error_messages`: vlastní text validační chyby.

Dokumentace `ForeignKey`:
https://docs.djangoproject.com/en/6.0/ref/models/fields/#foreignkey

### Ověření kroku
Krok je hotový, když se `models.py` uloží bez chyby a editor nezvýrazňuje problém v definici `recenzent`.

---

## Krok 4: Přidejte vazbu na knihu (`ForeignKey`)

### Kód pro tento krok
Přidejte hned pod `recenzent`:

```python
kniha = models.ForeignKey(
	Kniha,
	on_delete=models.CASCADE,
	verbose_name='Kniha',
	help_text='Vyberte recenzovanou knihu',
	error_messages={'null': 'Kniha musí být vybrána'}
)
```

### Vysvětlení
Stejný princip jako u recenzenta: jedna kniha může mít více recenzí.

### Ověření kroku
Krok je hotový, když model obsahuje obě vazby `recenzent` i `kniha` jako `ForeignKey`.

---

## Krok 5: Přidejte povinný text recenze

### Kód pro tento krok
Pod pole `kniha` vložte:

```python
text = models.TextField(
	verbose_name='Text recenze',
	help_text='Napište text recenze knihy',
	error_messages={'blank': 'Text recenze je povinný'}
)
```

### Vysvětlení
- `TextField`: vhodný pro delší text bez pevné délky.
- `blank=False` je u Django polí výchozí, proto je pole povinné i bez explicitního zápisu.
- `error_messages['blank']`: přívětivější hláška při prázdném vstupu.

Dokumentace `TextField`:
https://docs.djangoproject.com/en/6.0/ref/models/fields/#textfield

### Ověření kroku
Krok je hotový, když pole `text` existuje a je povinné (bez `blank=True`).

---

## Krok 6: Přidejte hodnocení 0–5 s výchozí hodnotou

### Kód pro tento krok
Pod pole `text` přidejte:

```python
hodnoceni = models.IntegerField(
	choices=HODNOCENI_CHOICES,
	default=3,
	verbose_name='Hodnocení',
	help_text='Vyberte hodnocení od 0 do 5 hvězdiček',
	error_messages={'invalid_choice': 'Zvolte hodnocení v rozsahu 0 až 5'}
)
```

### Vysvětlení
- `IntegerField`: ukládá celé číslo.
- `choices=...`: v adminu se vykreslí výběrový seznam.
- `default=3`: pokud uživatel nic nezvolí, uloží se hodnota 3.
- `invalid_choice`: vlastní text chyby při neplatné hodnotě.

Dokumentace `IntegerField`:
https://docs.djangoproject.com/en/6.0/ref/models/fields/#integerfield

### Ověření kroku
Krok je hotový, když `hodnoceni` používá `choices` a má `default=3`.

---

## Krok 7: Přidejte automatický čas poslední úpravy

### Kód pro tento krok
Pod pole `hodnoceni` přidejte:

```python
upraveno = models.DateTimeField(
	auto_now=True,
	verbose_name='Naposledy upraveno',
	help_text='Datum a čas poslední úpravy se nastaví automaticky'
)
```

### Vysvětlení
- `DateTimeField`: ukládá datum i čas.
- `auto_now=True`: při každém `save()` se hodnota automaticky přepíše na aktuální čas.

Pozor: `auto_now=True` se používá pro „čas poslední změny“.

Dokumentace `DateTimeField`:
https://docs.djangoproject.com/en/6.0/ref/models/fields/#datetimefield

### Ověření kroku
Krok je hotový, když pole `upraveno` používá `auto_now=True`.

---

## Typické chyby studentů a jak je poznat

- **Model nedědí z `models.Model`**: po `makemigrations` se model `Recenze` vůbec neobjeví.
- **Pole jsou mimo třídu (špatné odsazení)**: Django hlásí chybu importu nebo pole nejsou součástí modelu.
- **Použití `ManyToManyField` místo `ForeignKey`**: vztah neodpovídá zadání 1:N.
- **Chybí `choices` u `hodnoceni`**: v adminu není výběrový seznam, ale volný číselný vstup.
- **Chybí `default=3`**: nové recenze nemají výchozí hodnocení dle zadání.
- **Použití `auto_now_add` místo `auto_now`**: pole se neaktualizuje při úpravě recenze.

---

## Rychlá diagnostika (když něco nefunguje)

1. Spusťte `python manage.py check` a opravte první nahlášenou chybu.
2. Pokud model změny nejsou vidět, spusťte `python manage.py makemigrations` a `python manage.py migrate`.
3. Když je chyba v adminu, ověřte import modelu a `admin.site.register(...)`.
4. Při nejasném chování modelu otevřete shell (`python manage.py shell`) a zkuste `Recenze.objects.all()`.
5. Pokud se změny neprojeví, restartujte běžící server (`Ctrl+C` a znovu `python manage.py runserver`).

---

## Kompletní kód pro kontrolu (finální stav kroku A)

```python
class Recenze(models.Model):
	HODNOCENI_CHOICES = (
		(0, '☆☆☆☆☆'),
		(1, '★☆☆☆☆'),
		(2, '★★☆☆☆'),
		(3, '★★★☆☆'),
		(4, '★★★★☆'),
		(5, '★★★★★'),
	)

	recenzent = models.ForeignKey(
		Autor,
		on_delete=models.CASCADE,
		verbose_name='Recenzent',
		help_text='Vyberte autora recenze',
		error_messages={'null': 'Recenzent musí být vybrán'}
	)
	kniha = models.ForeignKey(
		Kniha,
		on_delete=models.CASCADE,
		verbose_name='Kniha',
		help_text='Vyberte recenzovanou knihu',
		error_messages={'null': 'Kniha musí být vybrána'}
	)
	text = models.TextField(
		verbose_name='Text recenze',
		help_text='Napište text recenze knihy',
		error_messages={'blank': 'Text recenze je povinný'}
	)
	hodnoceni = models.IntegerField(
		choices=HODNOCENI_CHOICES,
		default=3,
		verbose_name='Hodnocení',
		help_text='Vyberte hodnocení od 0 do 5 hvězdiček',
		error_messages={'invalid_choice': 'Zvolte hodnocení v rozsahu 0 až 5'}
	)
	upraveno = models.DateTimeField(
		auto_now=True,
		verbose_name='Naposledy upraveno',
		help_text='Datum a čas poslední úpravy se nastaví automaticky'
	)
```
