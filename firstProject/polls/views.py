from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request,"index.html")

def index(request):
    return HttpResponse("Hello world, you are at the polls index")

def error(request):
    return HttpResponse("This is an error !!")