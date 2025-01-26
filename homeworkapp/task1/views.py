from django.shortcuts import render
from django.http import HttpResponse
from .models import Buyer
from .models import Game

from .forms import UserRegister
users = [i.name for i in list(Buyer.objects.all())]

def sign_up_by_django(request):
    form = UserRegister(request.POST)
    info = {}
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username not in users and password == repeat_password and age >= 18:
                Buyer.objects.create(name=f'{username}', balance=0, age=f'{age}')
                return HttpResponse(f'Приветствуем, {username}!')
            elif username in users:
                info['error'] = 'Пользователь уже существует'
            elif password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18 лет'
    return render(request, 'registration_page.html', info)

def sign_up_by_html(request):
    info = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = int(request.POST.get('age'))
        if username not in users and password == repeat_password and age >= 18:
            Buyer.objects.create(name=f'{username}', balance=0, age=f'{age}')
            return HttpResponse(f'Приветствуем, {username}!')
        elif username in users:
            info['error'] = 'Пользователь уже существует'
        elif password != repeat_password:
            info['error'] = 'Пароли не совпадают'
        elif age < 18:
            info['error'] = 'Вы должны быть старше 18 лет'
    return render(request, 'registration_page.html', info)
def main(request):
    return render(request, 'main.html')
def shop(request):
    title = 'Игры'
    list_of_games = [i for i in list(Game.objects.all())]
    context = {
        'title': title,
        'list': list_of_games
    }
    return render(request, 'shop.html', context)
def cart(request):
    return render(request, 'cart.html')

