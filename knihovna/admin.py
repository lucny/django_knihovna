from django.contrib import admin
from django.db.models import Count
from django.utils.safestring import mark_safe

from .forms import KnihaAdminForm
# Import modelu Recenze
from .models import Autor, Kniha, Vydavatelstvi, Zanr, Recenze

# admin.site.register(Autor)
@admin.register(Autor)

class AutorAdmin(admin.ModelAdmin):
    list_display = ('jmeno', 'prijmeni', 'narozeni', 'umrti', 'kniha_count')
    list_filter = ('jmeno', 'prijmeni')
    search_fields = ('jmeno', 'prijmeni')
    fieldsets = (
        (None, {
            'fields': ('jmeno', 'prijmeni', 'fotografie')
        }),
        ('Životopisné údaje', {
            'fields': ('narozeni', 'umrti', 'biografie'),
            'classes': ('collapse', 'bios',)
        })
    )

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.annotate(
            _kniha_count=Count("kniha", distinct=True),
        ).order_by("-_kniha_count")
        return queryset

    def kniha_count(self, obj):
        return obj._kniha_count

    kniha_count.short_description = "Počet knih"
    kniha_count.admin_order_field = "_kniha_count"


class BookAdmin(admin.ModelAdmin):
    form = KnihaAdminForm
    readonly_fields = ['display_obalka']
    fields = ['titul', 'autori', 'obsah', 'pocet_stran', 'vydavatelstvi', 'rok_vydani', 'obalka', 'display_obalka', 'zanry', 'editor']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(editor=request.user)

    def display_obalka(self, obj):
        if obj.obalka:
            return mark_safe('<img src="{url}" width="{height}">'.format(
                url=obj.obalka.url,
                height=200,
            ))
        else:
            return 'No Image'

    display_obalka.short_description = 'Obrázek obálky'


admin.site.register(Kniha, BookAdmin)

admin.site.register(Vydavatelstvi)
admin.site.register(Zanr)
admin.site.register(Recenze)

