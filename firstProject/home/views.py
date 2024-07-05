from django.shortcuts import render

def home(request):
    return render(request,"home.html")

def shop(request):
    return render(request,"shop.html")

def blogs(request):
    return render(request,"blogs.html")

def recipes(request):
    return render(request,"recipes.html")