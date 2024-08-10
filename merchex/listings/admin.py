from django.contrib import admin
from listings.models import Band, Listing


# Register your models here.


# Pour afficher les champs name, year_formed, genre dans l'admin
# Les classes ModelAdmin permettent de configurer la manière dont les objets du modèle sont affichés dans l'administration.
class BandAdmin(admin.ModelAdmin):
    # On renseigne les champs à afficher dans l'admin
    list_display = ("name", "year_formed", "genre")


class ListingAdmin(admin.ModelAdmin):
    list_display = ("title", "type", "year", "sold", "band")


# Pour afficher les champs name, type, year, description dans l'admin
admin.site.register(Band, BandAdmin)

admin.site.register(Listing, ListingAdmin)
