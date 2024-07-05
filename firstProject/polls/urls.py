from django.urls import path
from .views import *

urlpatterns = [
    path("",welcome, name="welcome"),
    path("index/",index, name = "index"),
    path("error/",error, name = "error")
]