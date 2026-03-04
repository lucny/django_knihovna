# Návod B — řazení a textová reprezentace modelu `Recenze`

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
Doplnit do modelu `Recenze`:
- výchozí řazení podle hodnocení sestupně,
- textovou reprezentaci (`__str__`) podle vzoru.

## Postup krok za krokem

---

## Krok 1: Přidejte `Meta` do modelu `Recenze`

### Kód pro tento krok
Do třídy `Recenze` vložte:

```python
class Meta:
    ordering = ['-hodnoceni']
    verbose_name = 'Recenze'
    verbose_name_plural = 'Recenze'
```

### Vysvětlení
- `ordering`: výchozí řazení querysetů tohoto modelu.
- `'-hodnoceni'`: mínus znamená sestupně (`5,4,3,2,1,0`).
- `verbose_name`, `verbose_name_plural`: texty v Django administraci.

Dokumentace `Meta`:
https://docs.djangoproject.com/en/6.0/ref/models/options/

### Ověření kroku
Krok je hotový, když je `class Meta` uvnitř `Recenze` a obsahuje `ordering = ['-hodnoceni']`.

---

## Krok 2: Přidejte metodu `__str__`

### Kód pro tento krok
Do stejné třídy vložte:

```python
def __str__(self):
    hvezdy = dict(self.HODNOCENI_CHOICES).get(self.hodnoceni, '')
    return f'{self.recenzent} | {self.text} | {self.upraveno:%d.%m.%Y %H:%M} | {hvezdy}'
```

### Vysvětlení
- `dict(self.HODNOCENI_CHOICES)`: převede dvojice na slovník pro rychlé mapování.
- `.get(self.hodnoceni, '')`: bezpečně vrátí hvězdičky i když by hodnota nebyla nalezena.
- `f-string`: formátovaný text, který se zobrazí v adminu i shellu.

Poznámka: pokud učitel vyžaduje jiný přesný formát, upravte jen text uvnitř `return`.

### Ověření kroku
Krok je hotový, když `str(Recenze.objects.first())` vrátí čitelný text bez chyby.

---

## Krok 3: Ověřte výsledek v shellu

### Kód pro tento krok

```bash
python manage.py shell
```

```python
from knihovna.models import Recenze
Recenze.objects.all()[:3]
```

### Vysvětlení
Tento výpis rychle ověří, že model vrací záznamy ve správném pořadí a že `__str__` funguje bez chyby.

### Ověření kroku
- záznamy se vrací od nejvyššího hodnocení,
- textová reprezentace je čitelná.

---

## Typické chyby studentů a jak je poznat

- **`class Meta` je mimo `Recenze`**: řazení se nepoužije, data se vrací v jiném pořadí.
- **Chybí `-` v `ordering`**: recenze jsou vzestupně (`0 → 5`) místo sestupně.
- **Chybný název pole v `ordering`**: při načítání querysetu vznikne chyba `FieldError`.
- **`__str__` vrací nečitelný text**: v adminu nejde poznat, jaká recenze je která.
- **`__str__` používá neexistující atribut**: padá při výpisu objektu (admin/shell).

---

## Rychlá diagnostika (když něco nefunguje)

1. Ověřte odsazení: `class Meta` i `def __str__` musí být uvnitř `class Recenze`.
2. Pokud řazení nefunguje, zkontrolujte přesný zápis `ordering = ['-hodnoceni']`.
3. Pokud padá výpis objektu, v shellu spusťte `Recenze.objects.first()` a opravte `__str__`.
4. Po změně modelu nezapomeňte na `makemigrations` a `migrate`.
5. V adminu ověřte skutečné pořadí záznamů a porovnejte s očekávaným řazením.

---

## Kompletní kód pro kontrolu (třída `Recenze`)

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

    class Meta:
        ordering = ['-hodnoceni']
        verbose_name = 'Recenze'
        verbose_name_plural = 'Recenze'

    def __str__(self):
        hvezdy = dict(self.HODNOCENI_CHOICES).get(self.hodnoceni, '')
        return f'{self.recenzent} | {self.text} | {self.upraveno:%d.%m.%Y %H:%M} | {hvezdy}'
```
