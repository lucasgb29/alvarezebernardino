from django.shortcuts import render

def index(request):
    return render(request, 'alvarezebernardino/index.html')

def servicos(request):
    return render(request, 'alvarezebernardino/servicos.html')
