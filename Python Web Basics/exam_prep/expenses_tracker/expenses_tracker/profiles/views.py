from django.shortcuts import render

# Create your views here.
def show_profile(request):
    return render(request, 'profile.html')


def edit_profile(request, id):
    return render(request, 'profile-edit.html')


def delete_profile(request, id):
    return render(request, 'profile-delete.html')