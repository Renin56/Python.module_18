from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def shop(request):
    title = 'Магазин игр'
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

    return render(request, 'shop.html', context)


def basket(request):
    return render(request, 'basket.html')
