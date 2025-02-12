"""
URL configuration for UrbanProject2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from task1.views import index
from task2.views import class_view, func_view
from task3.views import shop_games, games, cart
from task4.views import shop_games_task4, games_task4, cart_task4
from task5.views import registration_page, sign_up_by_django, sign_up_by_html



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('func/', func_view),
    path('class/', class_view.as_view()),
    path('platform/', shop_games),
    path('platform/games/', games),
    path('platform/cart/', cart),
    path('platform4/', shop_games_task4),
    path('platform4/games/', games_task4),
    path('platform4/cart/', cart_task4),
    path('registration_django/', sign_up_by_django),
    path('registration_html/', sign_up_by_html),

]
