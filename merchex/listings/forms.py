from django import forms
from listings.models import Band, Listing


class ContactUsForm(forms.Form):
    name = forms.CharField(required=False, label="Votre nom")
    email = forms.EmailField(label="Votre email")
    message = forms.CharField(
        max_length=1000,
        widget=forms.Textarea,
        label="Votre message",
        help_text="1000 caractères max.",
    )


class BandForm(forms.ModelForm):
    class Meta:
        model = Band
        fields = "__all__"
        # Exclure des champs du modelForm
        exclude = ("active", "offficial_page")
        labels = {
            "name": "Nom",
            "genre": "Genre",
            "biography": "Biographie",
            "year_formed": "Année de formation",
        }


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = "__all__"
        labels = {
            "title": "Titre",
            "type": "Type",
            "year": "Année",
            "description": "Description",
            "sold": "Vendu",
            "band": "Groupe",
        }
