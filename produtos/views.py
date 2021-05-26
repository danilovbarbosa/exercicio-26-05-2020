from django.shortcuts import render

def index(request):
    context = {}
    return render(request, 'index.html', context=context)

def categorias(request):
    context = {}
    return render(request, 'categorias.html', context=context)