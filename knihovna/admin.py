from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Autor, Kniha, Recenze, Vydavatelstvi, Vypujcka, Zanr

admin.site.register(Autor)
admin.site.register(Kniha)
admin.site.register(Vydavatelstvi)
admin.site.register(Zanr)


@admin.register(Recenze)
class RecenzeAdmin(admin.ModelAdmin):
	list_display = ('recenzent', 'kniha', 'hodnoceni', 'upraveno')
	list_filter = ('hodnoceni', 'upraveno')
	search_fields = ('text', 'kniha__titul', 'recenzent__username', 'recenzent__first_name', 'recenzent__last_name', 'recenzent__email')


@admin.register(Vypujcka)
class VypujckaAdmin(admin.ModelAdmin):
	# list_display určuje sloupce v tabulce seznamu v adminu.
	list_display = ('ctenar_jmeno_admin', 'kniha', 'stav', 'datum_vypujcky', 'termin_vraceni', 'je_po_terminu_admin')
	# list_filter zpřístupní vpravo rychlé filtry podle stavu a data výpůjčky.
	list_filter = ('stav', 'datum_vypujcky')
	# search_fields umožní fulltextové hledání podle čtenáře a názvu knihy.
	search_fields = ('ctenar__username', 'ctenar__first_name', 'ctenar__last_name', 'ctenar__email', 'kniha__titul')

	@admin.display(description='Čtenář')
	def ctenar_jmeno_admin(self, obj):
		return obj.ctenar_jmeno()

	def formfield_for_foreignkey(self, db_field, request, **kwargs):
		if db_field.name == 'ctenar':
			user_model = get_user_model()
			kwargs['queryset'] = user_model.objects.filter(groups__name='readers').order_by('username')
		return super().formfield_for_foreignkey(db_field, request, **kwargs)

	@admin.display(boolean=True, description='Po termínu')
	def je_po_terminu_admin(self, obj):
		return obj.je_po_terminu()