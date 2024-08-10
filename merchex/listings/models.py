from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.


class Band(models.Model):

    # Pour afficher le nom du groupe dans l'admin : ceci n'est plus nécessaire si on utilise un ModelAdmin
    # Mais nous utilisons des clés étrangères pour les relations entre les modèles Band et Listing il faut donc le renseigner pour avoir
    # un affichage plus pertinent dans l'admin
    def __str__(self):
        return f"{self.name}"

    class Genre(models.TextChoices):
        HIP_HOP = "HH"
        SYNTH_POP = "SP"
        ALTERNATIVE_ROCK = "AR"

    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(choices=Genre.choices, max_length=5)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
        validators=[MinValueValidator(1900), MaxValueValidator(2024)]
    )
    active = models.fields.BooleanField(default=True)
    offficial_page = models.fields.URLField(null=True, blank=True)


class Listing(models.Model):

    def __str__(self):
        return f"{self.title}"

    class Type(models.TextChoices):
        RECORDS = "records"
        CLOTHING = "clothing"
        POSTER = "posters"
        MISCELLANEOUS = "miscellaneous"

    title = models.fields.CharField(max_length=100)
    descprition = models.fields.CharField(max_length=200)
    sold = models.fields.BooleanField(default=False)
    year = models.fields.IntegerField(null=True)
    type = models.CharField(choices=Type.choices, max_length=20)
    band = models.ForeignKey(Band, null=True, on_delete=models.CASCADE)
