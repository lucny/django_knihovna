from django.db.models import Count, Q
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.utils.text import slugify

from .models import Autor, Kniha, Vypujcka, Zanr


def index(request):
    """Domovská stránka aplikace s filtrovaným seznamem knih podle zvoleného žánru."""
    zanr = 'povídky'
    context = {
        'nadpis': zanr,
        'knihy': Kniha.objects.order_by('rok_vydani').filter(zanry__nazev=zanr),
        'zanry': Zanr.objects.all()
    }
    return render(request, 'index.html', context=context)


def book_list(request):
    """Seznam knih se základními informacemi pro přehledové zobrazení."""
    knihy = Kniha.objects.select_related('vydavatelstvi').prefetch_related('autori').order_by('-rok_vydani', 'titul')
    return render(request, 'books_list.html', {'knihy': knihy})


def book_detail(request, pk):
    """Detail konkrétní knihy včetně autorů, žánrů a recenzí."""
    kniha = get_object_or_404(
        Kniha.objects.select_related('vydavatelstvi').prefetch_related('autori', 'zanry', 'recenze__recenzent'),
        pk=pk
    )
    return render(request, 'book_detail.html', {'kniha': kniha})


def author_list(request):
    """Seznam autorů."""
    autori = Autor.objects.order_by('prijmeni', 'jmeno')
    return render(request, 'authors_list.html', {'autori': autori})


def author_detail(request, pk):
    """Detail autora a seznam jeho knih."""
    autor = get_object_or_404(Autor, pk=pk)
    knihy_autora = Kniha.objects.filter(autori=autor).select_related('vydavatelstvi').order_by('-rok_vydani', 'titul')
    return render(request, 'author_detail.html', {'autor': autor, 'knihy_autora': knihy_autora})


def _reader_slug(reader_name):
    # Slug vytváří URL-safe variantu jména čtenáře.
    # Použijeme ASCII slug (bez diakritiky), aby odpovídal <slug:...> converteru.
    return slugify(reader_name)


def _reader_name_from_slug(reader_slug):
    # Nemáme samostatný model čtenáře, proto mapujeme slug zpět
    # porovnáním nad DISTINCT jmény z tabulky výpůjček.
    for reader_name in Vypujcka.objects.values_list('ctenar', flat=True).distinct():
        if _reader_slug(reader_name) == reader_slug:
            return reader_name
    raise Http404('Čtenář nenalezen.')


def _decorate_loan_for_ui(loan):
    # Připravíme prezentační metadata ve view, aby šablona obsahovala
    # minimum podmínek a zůstala přehledná.
    if loan.stav == Vypujcka.STAV_VRACENO:
        loan.status_badge_class = 'badge-success'
        loan.row_class = ''
    elif loan.je_po_terminu() or loan.stav == Vypujcka.STAV_PO_TERMINU:
        loan.status_badge_class = 'badge-danger'
        loan.row_class = 'table-danger'
    else:
        loan.status_badge_class = 'badge-warning'
        loan.row_class = ''


def loans_list(request):
    """Seznam výpůjček se zvýrazněním po termínu a odkazy na detail."""
    loans = list(
        Vypujcka.objects
        .select_related('kniha')
        .order_by('-datum_vypujcky', 'termin_vraceni')
    )

    for loan in loans:
        _decorate_loan_for_ui(loan)

    return render(request, 'loans_list.html', {'loans': loans})


def loan_detail(request, pk):
    """Detail konkrétní výpůjčky."""
    loan = get_object_or_404(Vypujcka.objects.select_related('kniha'), pk=pk)
    _decorate_loan_for_ui(loan)
    return render(request, 'loan_detail.html', {'loan': loan})


def readers_list(request):
    """Přehled čtenářů odvozený z tabulky výpůjček s agregovanými počty."""
    readers_queryset = (
        Vypujcka.objects
        .values('ctenar')
        .annotate(
            total_loans=Count('id'),
            active_loans=Count('id', filter=Q(stav=Vypujcka.STAV_VYPUJCENO)),
            overdue_loans=Count('id', filter=Q(stav=Vypujcka.STAV_PO_TERMINU)),
        )
        .order_by('ctenar')
    )

    # Každý řádek rozšíříme o slug, aby šablona nemusela řešit transformaci jména.
    readers = [
        {
            **reader,
            'reader_slug': _reader_slug(reader['ctenar']),
        }
        for reader in readers_queryset
    ]

    return render(request, 'readers_list.html', {'readers': readers})


def reader_detail(request, reader_slug):
    """Detail čtenáře a jeho výpůjček podle slug URL."""
    reader = _reader_name_from_slug(reader_slug)

    # get_object_or_404 zaručí 404 i v případě, že mezitím čtenář zmizí z dat.
    get_object_or_404(Vypujcka.objects.filter(ctenar=reader))

    reader_loans = list(
        Vypujcka.objects
        .filter(ctenar=reader)
        .select_related('kniha')
        .order_by('-datum_vypujcky', 'termin_vraceni')
    )
    for loan in reader_loans:
        _decorate_loan_for_ui(loan)

    return render(
        request,
        'reader_detail.html',
        {
            'reader': reader,
            'reader_loans': reader_loans,
        },
    )
