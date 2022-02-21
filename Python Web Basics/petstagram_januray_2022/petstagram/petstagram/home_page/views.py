from django.shortcuts import render

# Create your views here.
from petstagram.profiles.views import get_profile


def home_page(request):
    profile = get_profile()

    context = {
        'has_profile': bool(profile),
        'profile': profile,
    }

    return render(request, 'home_page.html', context)