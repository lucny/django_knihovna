# Návod E — detail knihy podle ID

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
Vytvořit stránku detailu knihy, která se bude otevírat podle ID v URL.

Zadání používá adresu `/books/<id knihy>`, v projektu ale zároveň běží aplikace pod `/knihovna/`. V návodu proto nastavíme obě varianty:
- `/knihovna/books/<id>/`
- `/books/<id>/` (alias)

## Postup krok za krokem

---

## Krok 1: Přidejte pohled `book_detail`

### Kód pro tento krok
Do `knihovna/views.py` vložte:

```python
def book_detail(request, pk):
    kniha = get_object_or_404(
        Kniha.objects.select_related('vydavatelstvi').prefetch_related('autori', 'zanry'),
        pk=pk
    )
    return render(request, 'book_detail.html', {'kniha': kniha})
```

### Vysvětlení
- `pk`: primární klíč předaný z URL.
- `get_object_or_404(queryset, pk=pk)`: vrátí objekt nebo HTTP 404.
- `select_related('vydavatelstvi')`: optimalizace pro `ForeignKey`.
- `prefetch_related('autori', 'zanry')`: optimalizace pro M:N vazby.
- `render(..., {'kniha': kniha})`: předání objektu do šablony.

### Ověření kroku
Krok je hotový, když detail existující knihy vrátí 200 a neexistující vrátí 404.

Dokumentace `get_object_or_404`:
https://docs.djangoproject.com/en/6.0/topics/http/shortcuts/#get-object-or-404

---

## Krok 2: Přidejte URL do `knihovna/urls.py`

### Kód pro tento krok

```python
path('books/<int:pk>/', views.book_detail, name='book_detail'),
```

### Vysvětlení
- `<int:pk>`: URL converter na celé číslo.
- `name='book_detail'`: umožní použít `{% url 'book_detail' ... %}`.

### Ověření kroku
Krok je hotový, když `{% url 'book_detail' 1 %}` v šabloně nevytváří chybu.

---

## Krok 3: Přidejte alias `/books/<id>/` v projektových URL

### Kód pro tento krok
V `mat_knihovna/urls.py`:

```python
from knihovna import views as knihovna_views
```

a do `urlpatterns`:

```python
path('books/<int:pk>/', knihovna_views.book_detail, name='book_detail_alias'),
```

### Vysvětlení
Tím splníte přesné znění zadání i při zachování struktury projektu.

### Ověření kroku
Krok je hotový, když funguje i adresa `/books/1/`.

---

## Krok 4: Vytvořte šablonu detailu knihy

### Kód pro tento krok
Vytvořte `knihovna/templates/book_detail.html`:

```html
{% extends 'base.html' %}

{% block title %}Detail knihy{% endblock %}

{% block content %}
<div class="row mt-3 mb-4">
    <div class="col-12 col-md-4 mb-3">
        <img src="{{ kniha.obalka.url }}" alt="{{ kniha.titul }}" class="img-fluid rounded border book-cover">
    </div>
    <div class="col-12 col-md-8">
        <h2>{{ kniha.titul }}</h2>

        <p class="mb-1"><strong>Rok vydání:</strong> {{ kniha.rok_vydani|default:'-' }}</p>
        <p class="mb-1"><strong>Počet stran:</strong> {{ kniha.pocet_stran|default:'-' }}</p>
        <p class="mb-1"><strong>Vydavatelství:</strong> {{ kniha.vydavatelstvi.nazev|default:'-' }}</p>

        <p class="mt-3"><strong>Autoři:</strong>
            {% for autor in kniha.autori.all %}
                <a href="{% url 'author_detail' autor.pk %}">{{ autor.jmeno }} {{ autor.prijmeni }}</a>{% if not forloop.last %}, {% endif %}
            {% empty %}
                <span class="text-muted">Bez autora</span>
            {% endfor %}
        </p>

        <p><strong>Žánry:</strong>
            {% for zanr in kniha.zanry.all %}
                <span class="badge badge-info">{{ zanr.nazev }}</span>
            {% empty %}
                <span class="text-muted">Bez žánru</span>
            {% endfor %}
        </p>

        <hr>
        <h5>Obsah</h5>
        <p>{{ kniha.obsah|default:'Obsah není vyplněn.' }}</p>
    </div>
</div>
{% endblock %}
```

### Vysvětlení
- `|default:'-'`: bezpečné zobrazení i při chybějících datech.
- `{% empty %}`: fallback větev, pokud není žádný autor/žánr.
- `img-fluid`: responzivní obrázek v Bootstrapu.

### Ověření kroku
Krok je hotový, když se stránka detailu knihy vykreslí bez chyby a zobrazí všechna pole.

---

## Typické chyby studentů a jak je poznat

- **Použití `Kniha.objects.get(...)` bez ošetření**: při špatném ID padá chyba místo 404.
- **Neshoda parametru URL a view (`id` vs `pk`)**: Django hlásí, že funkce dostala nečekaný argument.
- **Chybí alias `/books/<id>/`**: stránka funguje jen pod `/knihovna/...`, ale ne dle zadání.
- **Chybí `|default` v šabloně**: při prázdných datech se objevují nehezké prázdné hodnoty.
- **Špatný název šablony v `render`**: `TemplateDoesNotExist` při otevření detailu.

---

## Rychlá diagnostika (když něco nefunguje)

1. 404 na detailu: zkontrolujte `path('books/<int:pk>/', ...)` v `knihovna/urls.py`.
2. Nejde `/books/1/`: ověřte alias v `mat_knihovna/urls.py`.
3. 500 při otevření detailu: zkontrolujte název šablony `book_detail.html` v `render`.
4. Chyba argumentů view: sjednoťte parametr `pk` v URL i ve funkci.
5. Pokud data chybí jen někde, ověřte, že testujete existující ID knihy v databázi.

---

## Kompletní kód pro kontrolu

`knihovna/views.py` obsahuje funkci `book_detail` z kroku 1.

`knihovna/urls.py` obsahuje:

```python
path('books/<int:pk>/', views.book_detail, name='book_detail'),
```

`mat_knihovna/urls.py` obsahuje alias:

```python
path('books/<int:pk>/', knihovna_views.book_detail, name='book_detail_alias'),
```

`knihovna/templates/book_detail.html` odpovídá kódu z kroku 4.

