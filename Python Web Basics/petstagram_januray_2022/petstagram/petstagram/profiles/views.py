from django.shortcuts import render

# Create your views here.
from petstagram.pets.models import PetPhoto
from petstagram.profiles.models import Profile


def get_profile():
    profile = Profile.objects.all()

    if profile:
        return profile[0]
    return None


def show_profile(request):
    profile = get_profile()

    pet_photos = PetPhoto.objects.filter(tagged_pets__user_profile=profile)
    total_likes = sum([x.likes for x in pet_photos])


    context = {
        'profile': profile,
        'pet_photos_count': len(pet_photos),
        'total_likes': total_likes,
        'pet_photos': pet_photos,
    }

    return render(request, 'profile_details.html', context)