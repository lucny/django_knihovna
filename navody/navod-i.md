# Návod I — Bootstrap a vlastní CSS

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
Přiblížit vzhled předloze a zachovat responzivní zobrazení.

## Postup krok za krokem

---

## Krok 1: Upravte `base.html` pro správné načítání stylů

### Kód pro tento krok
Soubor `knihovna/templates/base.html`:

```html
<!DOCTYPE html>
<html lang="cs">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}Školní knihovna{% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'bootstrap/bootstrap.min.css' %}">
    <link rel="stylesheet" href="{% static 'css/styles.css' %}">
</head>
<body>
    {% include 'page/header.html' %}
    {% include 'page/navbar.html' %}

    <main class="container">
        {% block content %}{% endblock %}
    </main>

    {% include 'page/footer.html' %}

    <script src="{% static 'bootstrap/jquery-3.3.1.slim.min.js' %}"></script>
    <script src="{% static 'bootstrap/popper.min.js' %}"></script>
    <script src="{% static 'bootstrap/bootstrap.min.js' %}"></script>
</body>
</html>
```

### Vysvětlení
- `viewport` je nutný pro mobilní zařízení.
- `{% load static %}` a `{% static ... %}` načítají statické soubory správnou cestou.

### Ověření kroku
Krok je hotový, když se načte Bootstrap i `styles.css` bez 404 chyb.

---

## Krok 2: Doplňte vlastní styly

### Kód pro tento krok
Soubor `knihovna/static/css/styles.css`:

```css
header {
    background-image: url('../img/book-logo.png');
    background-repeat: no-repeat;
    background-position: left 30px center;
}

main.container {
    min-height: 70vh;
}

.table td,
.table th {
    vertical-align: middle;
}

.card-img-top {
    height: 280px;
    object-fit: cover;
}

.book-cover,
.author-photo {
    max-height: 420px;
    object-fit: cover;
    width: 100%;
}

@media (max-width: 767.98px) {
    header {
        background-position: center 10px;
        padding-top: 70px;
    }

    .card-img-top {
        height: 220px;
    }
}
```

### Vysvětlení
- `object-fit: cover`: obrázek vyplní prostor bez deformace poměru stran.
- `@media`: úpravy jen pro menší obrazovky.

### Ověření kroku
Krok je hotový, když se vzhled mění při přepnutí mezi mobilem a desktopem.

---

## Krok 3: Propojte CSS třídy v detailových šablonách

### Kód pro tento krok
V `book_detail.html`:

```html
<img src="{{ kniha.obalka.url }}" alt="{{ kniha.titul }}" class="img-fluid rounded border book-cover">
```

V `author_detail.html`:

```html
<img src="{{ autor.fotografie.url }}" alt="{{ autor.jmeno }} {{ autor.prijmeni }}" class="img-fluid rounded border author-photo">
```

### Vysvětlení
Třídy `book-cover` a `author-photo` aplikují pravidla z `styles.css`.

### Ověření kroku
Krok je hotový, když obrázky v detailech nepřetékají a drží správný poměr stran.

---

## Typické chyby studentů a jak je poznat

- **Chybí `<meta name="viewport">`**: stránka je na mobilu zmenšená a špatně čitelná.
- **Nenahraný `styles.css` v `base.html`**: vlastní grafické úpravy se vůbec neprojeví.
- **Použití tříd v HTML bez definice v CSS**: očekávaná úprava vzhledu se neaplikuje.
- **Pevné rozměry bez `object-fit`**: obrázky jsou deformované nebo přetékají.
- **Chybějící media query**: layout na menších displejích neodpovídá zadání.

---

## Rychlá diagnostika (když něco nefunguje)

1. Pokud se styl nemění, ověřte načtení `styles.css` v nástrojích prohlížeče.
2. Pokud je mobilní zobrazení špatné, ověřte přítomnost `viewport` meta tagu.
3. Pokud přetékají obrázky, zkontrolujte třídy `book-cover`, `author-photo`, `card-img-top`.
4. Pokud se rozpadá layout, ověřte správné použití Bootstrap gridu (`row` + `col-*`).
5. Po úpravě CSS vždy obnovte stránku natvrdo (`Ctrl+F5`), aby se nebral starý cache obsah.

---

## Kompletní kód pro kontrolu
Použijte kód z kroků 1–3.
