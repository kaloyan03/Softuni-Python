from django.shortcuts import render, redirect
from petstagram.pets.models import Pet, Like, Comment
from petstagram.pets.forms import CreatePetForm, EditPetForm, CommentForm


# Create your views here.


def list_pets(request):
    all_pets = Pet.objects.all()

    context = {
        "pets": all_pets,
        "current_path": request.path,
    }

    return render(request, 'pets_page_template/index.html', context)


def pet_details(request, pk):
    pet = Pet.objects.get(pk=pk)
    pet_likes_count = pet.like_set.count
    comment_form = CommentForm()
    owner_name = pet.user
    all_likes = Like.objects.all()
    already_liked = False

    for like in all_likes:
        if like.pet_id == pet.id and like.user_id == request.user.id:
            already_liked = True
            break

    context = {
        "pet": pet,
        "pet_likes_count": pet_likes_count,
        'form': comment_form,
        'comments': pet.comment_set.all(),
        "current_path": request.path,
        "is_owner": owner_name == request.user,
        "owner_name": owner_name,
        "already_liked": already_liked
    }

    return render(request, 'pets_details_template/index.html', context)


def like_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    like_object_by_user = pet.like_set.filter(user_id=request.user.id)

    if not like_object_by_user:
        like = Like(
            pet=pet,
            user_id=request.user.id
            )
        like.save()
    else:
        like_object_by_user.delete()

    return redirect('pet details', pet.id)


def create_pet(request):
    if request.method == 'GET':
        form = CreatePetForm()

        context = {
            'form': form,
            "current_path": request.path,
        }

        return render(request, 'pet_create.html', context)
    else:
        form = CreatePetForm(request.POST, request.FILES)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect('list pets')


def edit_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    if request.method == 'GET':
        form = EditPetForm(initial=pet.__dict__)
        context = {
            'form': form,
            'pet_id': pet.id,
            "current_path": request.path,
        }

        return render(request, 'pet_edit.html', context)
    else:
        form = EditPetForm(request.POST, instance=pet)

        if form.is_valid():
            form.save()
            return redirect('pet details', pet.id)


def delete_pet(request, pk):
    pet = Pet.objects.get(pk=pk)

    if request.method == 'GET':
        context = {
            'pet_name': pet.name,
            "current_path": request.path,
        }

        return render(request, 'pet_delete.html', context)

    else:
        pet.delete()
        return redirect('list pets')


def comment_pet(request, pk):
    pet = Pet.objects.get(pk=pk)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = Comment(
            comment=form.cleaned_data['comment'],
            pet= pet,
            user_id=request.user.id,
        )
        comment.save()

    return redirect('pet details', pet.id)

