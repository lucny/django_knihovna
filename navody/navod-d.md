# Návod D — stránka Seznam knih na adrese `/knihovna/books/`

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
Vytvořit stránku s tabulkou knih, kde:
- seznam je seřazen podle roku vydání sestupně,
- titul knihy odkazuje na detail knihy,
- autoři jsou zkráceně (`J. Příjmení`) a odkazují na detail autora.

## Postup krok za krokem

---

## Krok 1: Přidejte pohled `book_list` do `views.py`

### Kód pro tento krok
Do `knihovna/views.py` vložte:

```python
def book_list(request):
    knihy = Kniha.objects.prefetch_related('autori').order_by('-rok_vydani', 'titul')
    context = {'knihy': knihy}
    return render(request, 'books_list.html', context)
```

### Vysvětlení
- `request`: objekt HTTP požadavku.
- `Kniha.objects...`: ORM dotaz na knihy.
- `prefetch_related('autori')`: přednačte M:N autory efektivněji.
- `order_by('-rok_vydani', 'titul')`: hlavní řazení rok sestupně, sekundární podle názvu.
- `context`: slovník dat pro šablonu.
- `render(request, template, context)`: vrátí HTML odpověď.

### Ověření kroku
Krok je hotový, když `book_list` vrací šablonu `books_list.html` s klíčem `knihy`.

Dokumentace QuerySet API:
https://docs.djangoproject.com/en/6.0/ref/models/querysets/

---

## Krok 2: Namapujte URL cestu

### Kód pro tento krok
Do `knihovna/urls.py` přidejte řádek:

```python
path('books/', views.book_list, name='book_list'),
```

### Vysvětlení
- první argument `'books/'`: část URL v rámci aplikace.
- druhý argument `views.book_list`: funkce pohledu.
- `name='book_list'`: jméno pro reverzní generování URL v šablonách.

### Ověření kroku
Krok je hotový, když URL `/knihovna/books/` přestane vracet 404.

Dokumentace URL dispatcheru:
https://docs.djangoproject.com/en/6.0/topics/http/urls/

---

## Krok 3: Vytvořte šablonu `books_list.html`

### Kód pro tento krok
Vytvořte soubor `knihovna/templates/books_list.html` s obsahem:

```html
{% extends 'base.html' %}

{% block title %}Seznam knih{% endblock %}

{% block content %}
<h2 class="mt-3 mb-3">Seznam knih</h2>

<div class="table-responsive">
    <table class="table table-striped table-hover">
        <thead class="thead-dark">
            <tr>
                <th>Titul</th>
                <th>Autoři</th>
                <th>Rok vydání</th>
                <th>Vydavatelství</th>
            </tr>
        </thead>
        <tbody>
            {% for kniha in knihy %}
            <tr>
                <td><a href="{% url 'book_detail' kniha.pk %}">{{ kniha.titul }}</a></td>
                <td>
                    {% for autor in kniha.autori.all %}
                        <a href="{% url 'author_detail' autor.pk %}">{{ autor.jmeno|slice:':1' }}. {{ autor.prijmeni }}</a>{% if not forloop.last %}, {% endif %}
                    {% empty %}
                        <span class="text-muted">Bez autora</span>
                    {% endfor %}
                </td>
                <td>{{ kniha.rok_vydani }}</td>
                <td>{{ kniha.vydavatelstvi.nazev|default:'-' }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</div>
{% endblock %}
```

### Vysvětlení
- `{% extends 'base.html' %}`: dědění společného layoutu.
- `{% for kniha in knihy %}`: cyklus přes knihy z `context`.
- `{% url 'book_detail' kniha.pk %}`: bezpečné generování URL detailu.
- `|slice:':1'`: zkrácení jména na iniciálu.
- `|default:'-'`: náhradní hodnota, pokud chybí vydavatelství.

### Ověření kroku
Krok je hotový, když tabulka zobrazuje knihy i autory a odkazy jsou klikatelné.

Dokumentace šablon:
https://docs.djangoproject.com/en/6.0/topics/templates/

---

## Krok 4: Ověřte stránku

### Kód pro tento krok

```bash
python manage.py runserver
```

Otevřete:
- `http://127.0.0.1:8000/knihovna/books/`

### Vysvětlení
Tento krok ověřuje výslednou integraci: view + URL + šablona + data z databáze.

### Ověření kroku
- tabulka se vykreslí bez chyby,
- knihy jsou od nejnovějších,
- odkazy na detail knihy a autora fungují.

---

## Typické chyby studentů a jak je poznat

- **Řazení bez `-` u roku**: knihy jsou od nejstarších místo od nejnovějších.
- **Chybí `name='book_list'` v URL**: `{% url 'book_list' %}` vyhodí `NoReverseMatch`.
- **Špatné jméno URL v šabloně**: odkazy v tabulce nefungují.
- **Zapomenutý `prefetch_related('autori')`**: stránka je pomalejší při větším počtu záznamů.
- **Šablona není ve správné složce `templates`**: Django hlásí `TemplateDoesNotExist`.

---

## Rychlá diagnostika (když něco nefunguje)

1. `NoReverseMatch`: porovnejte `name='book_list'` v `urls.py` s `{% url 'book_list' %}` v šabloně.
2. `TemplateDoesNotExist`: ověřte cestu `knihovna/templates/books_list.html`.
3. 404 na `/knihovna/books/`: zkontrolujte `path('books/', views.book_list, ...)`.
4. Špatné pořadí knih: ověřte `order_by('-rok_vydani', 'titul')`.
5. Při pomalém načítání ověřte, že ve view zůstalo `prefetch_related('autori')`.

---

## Kompletní kód pro kontrolu

`knihovna/views.py` (relevantní část):

```python
from django.shortcuts import get_object_or_404, render
from .models import Autor, Kniha, Zanr


def book_list(request):
    knihy = Kniha.objects.prefetch_related('autori').order_by('-rok_vydani', 'titul')
    context = {'knihy': knihy}
    return render(request, 'books_list.html', context)
```

`knihovna/urls.py` (relevantní část):

```python
path('books/', views.book_list, name='book_list'),
```

`knihovna/templates/books_list.html`: viz kód v kroku 3.
