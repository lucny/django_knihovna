from django.shortcuts import render
from django.views.generic import ListView

from .models import Kniha, Zanr


def index(request):
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)


# Přidání třídy BooksListView, která dědí z generické třídy ListView
# Pohled zobrazuje seznam knih
class BooksListView(ListView):
    model = Kniha
    template_name = 'books/books_list.html'
    context_object_name = 'books'
    ordering = ['-rok_vydani']