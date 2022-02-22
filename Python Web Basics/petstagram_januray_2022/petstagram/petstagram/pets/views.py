from django.shortcuts import render

# Create your views here.
from petstagram.pets.models import PetPhoto
from petstagram.profiles.views import get_profile


def pets_dashboard(request):
    profile = get_profile()

    pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile)

    context = {
        'pet_photos': pet_photos,
    }


    return render(request, 'dashboard.html', context)

def pets_photo_page(request, id):
    return render(request, 'photo_details.html')