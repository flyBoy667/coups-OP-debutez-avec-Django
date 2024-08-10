from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band
from listings.models import Listing
from listings.forms import BandForm, ContactUsForm, ListingForm
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages


# Create your views here.


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", context={"bands": bands})


# Si vous nommez votre entier correspondant id dans votre modèle d'URL et votre vue, sachez qu'il « masquera » ou
# « fera de l’ombre » à la fonction id intégrée de Python. Ce n'est peut-être pas un problème pour vous si vous n'aviez pas
# l'intention d'utiliser cette fonction de toute façon, mais si vous voulez éviter de la masquer, vous pouvez utiliser un nom plus
# spécifique : band_id. Votre chemin serait donc bands/<int:band_id>/ et vous définiriez votre fonction avec def band_detail(request, band_id):.
def band_detail(request, band_id):
    band = Band.objects.get(id=band_id)
    return render(request, "listings/band_detail.html", context={"band": band})


def band_create(request):
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect("band-detail", band_id=band.id)
    else:
        form = BandForm()

    return render(request, "listings/band_create.html", {"form": form})


def band_update(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == "POST":
        # Pour preemplir le form avec le band on utilise instance
        form = BandForm(request.POST, instance=band)

        if form.is_valid():
            band = form.save()
            return redirect("band-detail", band_id=band.id)
    else:
        # Pour remplir le form avec le band on utilise instance
        form = BandForm(instance=band)

    return render(request, "listings/band_update.html", {"form": form})


def band_delete(request, band_id):
    band = Band.objects.get(id=band_id)

    if request.method == "POST":
        band.delete()
        messages.error(
            request,
            "Group deleted",
        )
        return redirect("band-list")

    return render(request, "listings/band_delete.html", {"band": band})


def listing_detail(request, listing_id):
    listing = Listing.objects.get(id=listing_id)
    return render(request, "listings/listing_detail.html", context={"listing": listing})


def listing_create(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect("listing-detail", listing_id=listing.id)
    else:
        form = ListingForm()

    return render(request, "listings/listing_create.html", {"form": form})


def listing_update(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)

        if form.is_valid():
            listing = form.save()
            return redirect("listing-detail", listing_id=listing.id)
    else:
        form = ListingForm(instance=listing)

    return render(request, "listings/listing_update.html", {"form": form})


def listing_delete(request, listing_id):
    listing = Listing.objects.get(id=listing_id)

    if request.method == "POST":
        listing.delete()
        messages.error(
            request,
            "Listing deleted",
        )
        return redirect("listing-list")

    return render(request, "listings/listing_delete.html", {"listing": listing})


def about(request):
    return render(request, "listings/about.html")


def listing(request):
    listings = Listing.objects.all()
    return render(
        request,
        "listings/listings.html",
        context={"listings": listings},
    )


def contact(request):

    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            send_mail(
                subject=f'Message de {data["name"] or "anonyme"} via le formulaire de contact MerchEx',
                message=data["message"],
                from_email=data["email"],
                recipient_list=["admin@merchex.xyz"],
            )
            return redirect("email-sent")

    else:
        form = ContactUsForm()

    return render(request, "listings/contact.html", {"form": form})


def email_sent(request):
    return render(request, "listings/email_sent.html")
