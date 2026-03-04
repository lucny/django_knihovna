# Návod G — správné mapování cest v `urls.py`

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
Zajistit správné URL mapování pro všechny nové stránky.

## Postup krok za krokem

---

## Krok 1: Upravte `knihovna/urls.py`

### Kód pro tento krok
Soubor `knihovna/urls.py` nastavte takto:

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:pk>/', views.book_detail, name='book_detail'),
    path('authors/', views.author_list, name='author_list'),
    path('authors/<int:pk>/', views.author_detail, name='author_detail'),
]
```

### Vysvětlení
- `name=...` je kritické pro `{% url %}` v šablonách.
- konzistentní názvy URL brání chybám typu `NoReverseMatch`.

### Ověření kroku
Krok je hotový, když všechny názvy URL lze použít v šablonách bez `NoReverseMatch`.

---

## Krok 2: Upravte `mat_knihovna/urls.py`

### Kód pro tento krok

```python
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from knihovna import views as knihovna_views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('knihovna/', include('knihovna.urls')),
    path('books/<int:pk>/', knihovna_views.book_detail, name='book_detail_alias'),
    path('', RedirectView.as_view(url='knihovna/')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### Vysvětlení
- `include('knihovna.urls')`: deleguje URL do aplikace.
- `RedirectView.as_view(url='knihovna/')`: root URL přesměruje na aplikaci.
- `static(...)`: v režimu DEBUG zpřístupní statické a media soubory.

### Ověření kroku
Krok je hotový, když funguje root `/`, aplikační cesty i načítání statických souborů.

---

## Krok 3: Ověření URL

### Kód pro tento krok

```bash
python manage.py runserver
```

Otestujte:
- `http://127.0.0.1:8000/knihovna/books/`
- `http://127.0.0.1:8000/knihovna/books/1/`
- `http://127.0.0.1:8000/books/1/`
- `http://127.0.0.1:8000/knihovna/authors/`
- `http://127.0.0.1:8000/knihovna/authors/1/`

### Vysvětlení
Jde o minimální test routingu, který ověří všechny kritické cesty vytvořené v úlohách D–G.

### Ověření kroku
Krok je hotový, když všech 5 adres vrací stránku bez chyby 500.

---

## Typické chyby studentů a jak je poznat

- **Chybí `include('knihovna.urls')`**: žádná aplikační URL není dostupná.
- **Duplicitní nebo špatné `name` u URL**: `{% url %}` selže nebo vrací jinou cestu.
- **Odebrané `static(...)` v DEBUG**: nefungují CSS/obrázky v lokálním běhu.
- **Alias `/books/<id>/` ukazuje na jiný view**: otevře se špatná stránka nebo chyba.
- **Nesprávný import `knihovna_views`**: projektové URL neprojdou při startu serveru.

---

## Rychlá diagnostika (když něco nefunguje)

1. Když nefunguje více URL najednou, začněte kontrolou `mat_knihovna/urls.py`.
2. Když nefungují odkazy v šablonách, ověřte jedinečnost a správnost `name=...`.
3. Když nejdou statické soubory, ověřte blok `if settings.DEBUG: ... static(...)`.
4. Při podezření na routing spusťte server a testujte URL jednu po druhé.
5. Pokud si nejste jistí, vraťte se na minimální funkční verzi URL a přidávejte cesty postupně.

---

## Kompletní kód pro kontrolu
Použijte přesně kód z kroků 1 a 2.
