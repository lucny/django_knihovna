# Import třídy Count pro agregaci dat
from django.db.models import Count
# Import metody render pro vykreslení šablon
from django.shortcuts import render
from django.urls import reverse_lazy
# Import generických tříd ListView a DetailView z modulu django.views.generic
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import KnihaForm
from .models import Kniha, Zanr, Autor


# Pohled pro zobrazení domovské stránky
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


# Přidání třídy BookDetailView, která dědí z generické třídy DetailView
# Pohled zobrazuje detail knihy
class BookDetailView(DetailView):
    model = Kniha
    template_name = 'books/book_detail.html'
    context_object_name = 'book'


# Přidání třídy BookCreateView, která dědí z generické třídy CreateView
# Pohled zobrazuje formulář pro vložení knihy
class BookCreateView(CreateView):
    model = Kniha
    template_name = 'books/book_bootstrap_form.html'
    fields = '__all__'
    form = KnihaForm
    success_url = reverse_lazy('books_list')


# Přidání třídy BookUpdateView, která dědí z generické třídy UpdateView
# Pohled zobrazuje formulář pro aktualizaci knihy
class BookUpdateView(UpdateView):
    model = Kniha
    template_name = 'books/book_bootstrap_form.html'
    fields = '__all__'
    form = KnihaForm
    context_object_name = 'book'
    success_url = reverse_lazy('books_list')


# Přidání třídy BookDeleteView, která dědí z generické třídy DeleteView
# Pohled zobrazuje formulář pro smazání knihy
class BookDeleteView(DeleteView):
    model = Kniha
    template_name = 'books/book_confirm_delete.html'
    context_object_name = 'book'
    success_url = reverse_lazy('books_list')


# Přidání třídy AuthorsListView, která dědí z generické třídy ListView
# Pohled zobrazuje seznam autorů
class AuthorsListView(ListView):
    model = Autor
    context_object_name = 'authors'
    queryset = Autor.objects.annotate(pocet_knih=Count('kniha')).order_by('-pocet_knih')
    template_name = 'authors/authors_list.html'


# Přidání třídy AuthorDetailView, která dědí z generické třídy DetailView
# Pohled zobrazuje detail autora
class AuthorDetailView(DetailView):
    model = Autor
    template_name = 'authors/author_detail.html'
    context_object_name = 'author'


