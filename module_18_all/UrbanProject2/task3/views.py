from django.shortcuts import render

# Create your views here.

def shop_games(request):
    return render(request, 'shop_game.html')

def games(request):
    title = 'Игры'
    game1 = 'Atomic Heart'
    game2 = 'Cyberpunk 2077'
    game3 = 'PayDay 2'
    home = ''
    context = {
        'title': title,
        'game1': game1,
        'game2': game2,
        'game3': game3,
        'home': home,
    }

    return render(request, 'games.html', context)

def cart(request):
    status = 'Извините, ваша корзина пуста'
    context = {
        'status': status,
    }
    return render(request, 'cart.html', context)
