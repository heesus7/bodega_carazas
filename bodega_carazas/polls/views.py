from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Hola esta es la primera app de la bodega carazas')