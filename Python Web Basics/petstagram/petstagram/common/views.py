from django.shortcuts import render


# Create your views here.
def landing_page(request):
    context = {
        'current_path': request.path,
    }
    return render(request, 'landing_page_template/index.html', context)

