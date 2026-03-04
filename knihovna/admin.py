from django.contrib import admin
from .models import Autor, Kniha, Recenze, Vydavatelstvi, Zanr

admin.site.register(Autor)
admin.site.register(Kniha)
admin.site.register(Vydavatelstvi)
admin.site.register(Zanr)


@admin.register(Recenze)
class RecenzeAdmin(admin.ModelAdmin):
	list_display = ('recenzent', 'kniha', 'hodnoceni', 'upraveno')
	list_filter = ('hodnoceni', 'upraveno')
	search_fields = ('text', 'kniha__titul', 'recenzent__jmeno', 'recenzent__prijmeni')