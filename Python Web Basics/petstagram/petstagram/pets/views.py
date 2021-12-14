from django.shortcuts import render, redirect
from petstagram.pets.models import Pet, Like


# Create your views here.


def list_pets(request):
    all_pets = Pet.objects.all()

    context = {
        "pets": all_pets,
    }

    return render(request, 'pets_page_template/index.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet_likes_count = pet.like_set.count

    context = {
        "pet": pet,
        "pet_likes_count": pet_likes_count,
    }

    return render(request, 'pets_details_template/index.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    like = Like(
        pet=pet
                )
    like.save()

    return redirect('pet details', pet.id)
