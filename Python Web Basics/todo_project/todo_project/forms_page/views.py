from django.shortcuts import render
from todo_project.forms_page.user_forms import UserForm
# Create your views here.


def show_form_data(request):
    if request.method == 'POST':
        form = UserForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            age = form.cleaned_data['age']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            text = form.cleaned_data['text']

            fields = {
                'name': name,
                'age': age,
                'email': email,
                'password': password,
                'text': text,
            }

            for key, value in fields.items():
                print(f'{key.upper()}: {value}')

        else:
            print(form.errors)

    else:
        context = {
            "form": UserForm(),
        }
        return render(request, 'form_template/index.html', context)