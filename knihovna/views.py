from django.db.models import Avg, Sum, Count, Min, Q, Max
from django.http import Http404
from django.shortcuts import render
from .models import Kniha, Zanr, Autor, Recenze


def index(request):
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)


def orm_tester(request):
    dotaz1 = Kniha.objects.order_by('rok_vydani').filter(zanry__nazev='povídky').values()
    dotaz2 = Kniha.objects.values('zanry__nazev').annotate(pocet_knih=Count('id')).annotate(
        prumer_stran=Avg('pocet_stran')).annotate(nejstarsi=Min('rok_vydani')).annotate(
        celkem_stran=Sum('pocet_stran')).order_by('-pocet_knih', 'nejstarsi')
    dotaz3 = Kniha.objects.values('vydavatelstvi__nazev').annotate(pocet_knih=Count('id')).annotate(
        celkem_stran=Sum('pocet_stran')).filter(Q(pocet_knih__gte=2) | Q(celkem_stran__lt=100)).order_by(
        '-pocet_knih', 'celkem_stran')
    try:
        data = dotaz1
        print(list(data.values()))
    except Kniha.DoesNotExist:
        raise Http404("Data nebyla nalezena")

    context = {
        'data': list(data),
        'sloupce': list(data.first().keys()),
    }
    return render(request, 'orm.html', context=context)

