# Návod H — pohledy ve `views.py`

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
Vytvořit všechny pohledy, které obslouží nové stránky.

## Postup krok za krokem

---

## Krok 1: Připravte importy

### Kód pro tento krok

```python
from django.shortcuts import get_object_or_404, render
from .models import Autor, Kniha, Zanr
```

### Vysvětlení
- `render`: vrací HTML odpověď.
- `get_object_or_404`: bezpečné načtení detailu.
- modely: přístup k databázi přes ORM.

### Ověření kroku
Krok je hotový, když importy projdou bez chyby při spuštění serveru.

---

## Krok 2: Přidejte všech 5 pohledů

### Kód pro tento krok
Do `knihovna/views.py` vložte:

```python
def index(request):
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)


def book_list(request):
    knihy = Kniha.objects.prefetch_related('autori').order_by('-rok_vydani', 'titul')
    return render(request, 'books_list.html', {'knihy': knihy})


def book_detail(request, pk):
    kniha = get_object_or_404(
        Kniha.objects.select_related('vydavatelstvi').prefetch_related('autori', 'zanry'),
        pk=pk
    )
    return render(request, 'book_detail.html', {'kniha': kniha})


def author_list(request):
    autori = Autor.objects.order_by('prijmeni', 'jmeno')
    return render(request, 'authors_list.html', {'autori': autori})


def author_detail(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    knihy_autora = Kniha.objects.filter(autori=autor).order_by('-rok_vydani', 'titul')
    return render(request, 'author_detail.html', {'autor': autor, 'knihy_autora': knihy_autora})
```

### Vysvětlení
- každý pohled vrací jednu konkrétní šablonu,
- detailové pohledy používají `get_object_or_404`,
- dotazy jsou optimalizované (`select_related`, `prefetch_related`).

### Ověření kroku
Krok je hotový, když každá funkce view vrací odpověď bez výjimky.

---

## Krok 3: Ověření

### Kód pro tento krok

```bash
python manage.py runserver
```

Zkontrolujte, že žádný nový pohled nevrací chybu 500.

### Vysvětlení
Tento krok ověřuje funkčnost všech přidaných view v reálném běhu aplikace.

### Ověření kroku
Krok je hotový, když stránky z úloh D–F načtete bez serverové chyby.

---

## Typické chyby studentů a jak je poznat

- **Chybějící import modelu ve `views.py`**: při otevření stránky vznikne `NameError`.
- **Překlep v názvu šablony v `render(...)`**: Django hlásí `TemplateDoesNotExist`.
- **Neoptimalizované dotazy u detailu**: stránka je pomalejší při větším objemu dat.
- **Vrácení špatného kontextu**: v šabloně chybí proměnné (`kniha`, `autor`, `knihy_autora`).
- **Nejednotné názvy funkcí vs URL**: při routování vznikají chyby nebo nefunkční odkazy.

---

## Rychlá diagnostika (když něco nefunguje)

1. 500 chyba po kliknutí: zkontrolujte traceback, obvykle jde o špatný import nebo název šablony.
2. Chybějící data v šabloně: ověřte, že view vrací správný klíč v kontextu.
3. Pomalé načítání detailu: ověřte použití `select_related`/`prefetch_related`.
4. Neaktivní URL: zkontrolujte, zda odpovídá název view v `urls.py`.
5. Pokud chyba přetrvává, otestujte view samostatně v shellu přes jednoduchý queryset.

---

## Kompletní kód pro kontrolu
Finální `knihovna/views.py` obsahuje importy z kroku 1 a funkce z kroku 2.
