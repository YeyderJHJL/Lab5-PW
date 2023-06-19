from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myHomeView(*args, **kwargs):
    return HttpResponse('<h1>Hola mundo desde django</h1>')
def anotherPage(request):
    return HttpResponse('<h1>Es otra página de django</h1>')
def myTemplate(request, *args, **kwargs):
    return render(request, 'home.html', {})