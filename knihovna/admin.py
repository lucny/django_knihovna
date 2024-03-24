from django.contrib import admin
# Import modelu Recenze
from .models import Autor, Kniha, Vydavatelstvi, Zanr, Recenze

admin.site.register(Autor)
admin.site.register(Kniha)
admin.site.register(Vydavatelstvi)
admin.site.register(Zanr)
# Registrace modelu Recenze
admin.site.register(Recenze)