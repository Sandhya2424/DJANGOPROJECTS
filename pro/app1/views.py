from django.http import HttpResponse
from django.shortcuts import render

#function based
#home view

def Home(request):
    return HttpResponse("Welcome to new django app")


#index view

def index(request):
    return HttpResponse("index page")