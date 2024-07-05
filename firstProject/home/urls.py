from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home,name = 'home'),
    path('shop/',shop,name = 'shop'),
    path('blogs/',blogs,name = 'blogs'),
    path('recipes/',recipes, name = 'recipes')
]