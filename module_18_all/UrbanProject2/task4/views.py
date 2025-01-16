from django.shortcuts import render

# Create your views here.

def shop_games_task4(request):
    return render(request, 'shop_game_task4.html')

def games_task4(request):
    games = ['Atomic Heart', 'Cyberpunk 2077', 'PayDay 2']
    context = {
        'games': games,
    }

    return render(request, 'games_task4.html', context)

def cart_task4(request):
    status = 'Извините, ваша корзина пуста'
    context = {
        'status': status,
    }
    return render(request, 'cart_task4.html', context)
