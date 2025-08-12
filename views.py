from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("home page")

def html(request):
    return render(request, "index.html")