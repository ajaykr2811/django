from django.urls import path
from .views import *

urlpatterns = [
    path("gs/",homePage,name="homepage")
]