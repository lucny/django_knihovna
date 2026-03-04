from django.shortcuts import get_object_or_404, render

from .models import Autor, Kniha, Zanr


def index(request):
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)


def book_list(request):
    knihy = Kniha.objects.select_related('vydavatelstvi').prefetch_related('autori').order_by('-rok_vydani', 'titul')
    return render(request, 'books_list.html', {'knihy': knihy})


def book_detail(request, pk):
    kniha = get_object_or_404(
        Kniha.objects.select_related('vydavatelstvi').prefetch_related('autori', 'zanry', 'recenze__recenzent'),
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
