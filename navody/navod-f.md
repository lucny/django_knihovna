# Návod F — galerie autorů a detail autora

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
Vytvořit:
- stránku s galerií autorů,
- stránku s podrobnostmi vybraného autora.

## Postup krok za krokem

---

## Krok 1: Přidejte pohled `author_list`

### Kód pro tento krok
Do `knihovna/views.py`:

```python
def author_list(request):
    autori = Autor.objects.order_by('prijmeni', 'jmeno')
    return render(request, 'authors_list.html', {'autori': autori})
```

### Vysvětlení
- `order_by('prijmeni', 'jmeno')`: čitelné řazení autorů abecedně.
- `{'autori': autori}`: kontext pro šablonu.

### Ověření kroku
Krok je hotový, když `author_list` vrací šablonu `authors_list.html` s daty autorů.

---

## Krok 2: Přidejte pohled `author_detail`

### Kód pro tento krok

```python
def author_detail(request, pk):
    autor = get_object_or_404(Autor, pk=pk)
    knihy_autora = Kniha.objects.filter(autori=autor).order_by('-rok_vydani', 'titul')
    return render(request, 'author_detail.html', {'autor': autor, 'knihy_autora': knihy_autora})
```

### Vysvětlení
- `filter(autori=autor)`: přes M:N vazbu vrátí knihy konkrétního autora.
- `knihy_autora`: samostatná proměnná do šablony pro přehledné zobrazení.

### Ověření kroku
Krok je hotový, když detail autora vrací i seznam jeho knih.

---

## Krok 3: Přidejte URL cesty

### Kód pro tento krok
Do `knihovna/urls.py`:

```python
path('authors/', views.author_list, name='author_list'),
path('authors/<int:pk>/', views.author_detail, name='author_detail'),
```

### Vysvětlení
- první URL zobrazí seznam,
- druhá URL detail vybraného autora podle ID.

### Ověření kroku
Krok je hotový, když fungují adresy `/knihovna/authors/` a `/knihovna/authors/1/`.

---

## Krok 4: Vytvořte šablonu galerie autorů

### Kód pro tento krok
Soubor `knihovna/templates/authors_list.html`:

```html
{% extends 'base.html' %}

{% block title %}Galerie autorů{% endblock %}

{% block content %}
<h2 class="mt-3 mb-3">Galerie autorů</h2>

<div class="row">
    {% for autor in autori %}
    <div class="col-12 col-sm-6 col-lg-4 mb-4">
        <div class="card h-100 shadow-sm">
            <img src="{{ autor.fotografie.url }}" class="card-img-top" alt="{{ autor.jmeno }} {{ autor.prijmeni }}">
            <div class="card-body d-flex flex-column">
                <h5 class="card-title">{{ autor.jmeno }} {{ autor.prijmeni }}</h5>
                <p class="card-text text-muted mb-3">
                    {% if autor.narozeni %}{{ autor.narozeni|date:'j. n. Y' }}{% else %}?{% endif %}
                    –
                    {% if autor.umrti %}{{ autor.umrti|date:'j. n. Y' }}{% else %}dosud{% endif %}
                </p>
                <a href="{% url 'author_detail' autor.pk %}" class="btn btn-outline-info mt-auto">Detail autora</a>
            </div>
        </div>
    </div>
    {% endfor %}
</div>
{% endblock %}
```

### Vysvětlení
Šablona používá Bootstrap karty a zobrazuje základní data autora včetně odkazu na detail.

### Ověření kroku
Krok je hotový, když galerie autorů zobrazí karty bez rozbitých odkazů.

---

## Krok 5: Vytvořte šablonu detailu autora

### Kód pro tento krok
Soubor `knihovna/templates/author_detail.html`:

```html
{% extends 'base.html' %}

{% block title %}Detail autora{% endblock %}

{% block content %}
<div class="row mt-3 mb-4">
    <div class="col-12 col-md-4 mb-3">
        <img src="{{ autor.fotografie.url }}" alt="{{ autor.jmeno }} {{ autor.prijmeni }}" class="img-fluid rounded border author-photo">
    </div>
    <div class="col-12 col-md-8">
        <h2>{{ autor.jmeno }} {{ autor.prijmeni }}</h2>
        <p><strong>Narození:</strong> {{ autor.narozeni|date:'j. n. Y'|default:'-' }}</p>
        <p><strong>Úmrtí:</strong> {{ autor.umrti|date:'j. n. Y'|default:'-' }}</p>

        <h5 class="mt-3">Biografie</h5>
        <p>{{ autor.biografie|default:'Biografie není vyplněna.' }}</p>

        <h5 class="mt-4">Knihy autora</h5>
        <ul class="list-group">
            {% for kniha in knihy_autora %}
            <li class="list-group-item d-flex justify-content-between align-items-center">
                <a href="{% url 'book_detail' kniha.pk %}">{{ kniha.titul }}</a>
                <span class="badge badge-secondary">{{ kniha.rok_vydani }}</span>
            </li>
            {% empty %}
            <li class="list-group-item text-muted">Autor nemá přiřazené žádné knihy.</li>
            {% endfor %}
        </ul>
    </div>
</div>
{% endblock %}
```

### Vysvětlení
Detail autora kombinuje osobní údaje s výpisem knih a fallbackem přes `{% empty %}`.

### Ověření kroku
Krok je hotový, když detail autora obsahuje biografii i funkční odkazy na knihy.

---

## Typické chyby studentů a jak je poznat

- **Záměna `author_list` a `author_detail`**: obě URL vracejí stejnou stránku.
- **Špatný filtr knih (`filter(autor=...)` místo `filter(autori=...)`)**: seznam knih autora je stále prázdný.
- **Chybí `{% empty %}` u seznamu knih**: stránka působí rozbitě, když autor nemá knihy.
- **Neplatná cesta k obrázku autora**: v šabloně se zobrazí rozbitý obrázek.
- **Nesoulad názvů URL v šablonách**: odkazy na detail autora nebo knihy nefungují.

---

## Rychlá diagnostika (když něco nefunguje)

1. 404 na autora: zkontrolujte `path('authors/<int:pk>/', ...)`.
2. Prázdný seznam knih autora: ověřte filtr `Kniha.objects.filter(autori=autor)`.
3. `TemplateDoesNotExist`: zkontrolujte, že existují `authors_list.html` a `author_detail.html`.
4. Rozbité obrázky: ověřte `MEDIA_URL`, `MEDIA_ROOT` a reálnou hodnotu `autor.fotografie`.
5. Pokud nefungují odkazy mezi stránkami, porovnejte názvy URL v `urls.py` a v šablonách.

---

## Kompletní kód pro kontrolu

Pohledy: kroky 1–2.

URL: krok 3.

Šablony: kroky 4–5.

