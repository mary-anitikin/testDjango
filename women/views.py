from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения women.")

def categories(request, cat):
    return HttpResponse(f"<h1>Статьи по категориям</h1>{cat}</p>")

def categoriesone(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")

def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1>{year}</p>")