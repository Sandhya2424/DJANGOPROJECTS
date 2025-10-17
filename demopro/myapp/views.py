from django.http import HttpResponse
from django.shortcuts import render


# def first(request):
#     return HttpResponse("first page")
#
#
# def second(request):
#     return HttpResponse("second page page")


def first(request):
    context={'name':'arun','age':23}
    return render(request,'first.html',context)

def second(request):
    context={'place':'ekm','gender':'male'}
    return render(request,'second.html',context)