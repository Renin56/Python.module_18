from django.shortcuts import render
from .forms import UserRegister
from django.http import HttpResponse

# Create your views here.

users = ['Alex', 'Max']

def registration_page(request):
    return render(request, 'registration_page.html')


def sign_up_by_django(request):
    info = {}

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = int(form.cleaned_data['age'])

            if username in users:
                info['error'] = 'Пользователь уже существует!'
                print(info)
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают!'
                print(info)
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет!'
                print(info)
            else:
                return HttpResponse(f'Приветствуем, {username}! (Django)')
            return HttpResponse(f'Ошибка регистрации: {info["error"]} (Django)')
        else:
            info['form'] = form
            print(info)
    else:
        form = UserRegister()
        info['form'] = form
        print(info)
    return render(request, 'registration_page.html', info)


def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))

        if password != repeat_password:
            info['error'] = 'Пароли не совпадают'
            print(info)
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
            print(info)
        elif username in users:
            info['error'] = 'Пользователь уже существует'
            print(info)
        else:
            return HttpResponse(f'Приветствуем, {username}! (HTML)')
        return HttpResponse(f'Ошибка регистрации: {info["error"]} (HTML)')

    return render(request, 'registration_page.html', info)