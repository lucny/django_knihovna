from django.contrib import admin
from .models import Autor, Kniha, Recenze, Vydavatelstvi, Vypujcka, Zanr

admin.site.register(Autor)
admin.site.register(Kniha)
admin.site.register(Vydavatelstvi)
admin.site.register(Zanr)


@admin.register(Recenze)
class RecenzeAdmin(admin.ModelAdmin):
	list_display = ('recenzent', 'kniha', 'hodnoceni', 'upraveno')
	list_filter = ('hodnoceni', 'upraveno')
	search_fields = ('text', 'kniha__titul', 'recenzent__jmeno', 'recenzent__prijmeni')


@admin.register(Vypujcka)
class VypujckaAdmin(admin.ModelAdmin):
	# list_display určuje sloupce v tabulce seznamu v adminu.
	list_display = ('ctenar', 'kniha', 'stav', 'datum_vypujcky', 'termin_vraceni', 'je_po_terminu_admin')
	# list_filter zpřístupní vpravo rychlé filtry podle stavu a data výpůjčky.
	list_filter = ('stav', 'datum_vypujcky')
	# search_fields umožní fulltextové hledání podle čtenáře a názvu knihy.
	search_fields = ('ctenar', 'kniha__titul')

	@admin.display(boolean=True, description='Po termínu')
	def je_po_terminu_admin(self, obj):
		return obj.je_po_terminu()