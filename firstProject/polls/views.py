from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request,"index.html")

def index(request):
    return HttpResponse("Hello world, you are at the polls index")

def error(request):
    return HttpResponse("This is an error !!")

def people_information(request):
    peoples = [
        {"Name" : "Varun Kumar","Age": 28, "Place" : "Bangalore"},
        {"Name" : "Sanjay ","Age": 20, "Place" : "Mysore"},
        {"Name" : "Kumar ","Age": 18, "Place" : "Delhi"},
        {"Name" : "Vipul ","Age": 14, "Place" : "Mumbai"},
        {"Name" : "Ram ","Age": 55, "Place" : "Jaipur"},
        {"Name" : "Sachin ","Age": 11, "Place" : "Bhopal"},
        {"Name" : "Rohit ","Age": 14, "Place" : "indor"}
    ]

    return render(request,"peopleInformation.html",context = {"peoples" : peoples})