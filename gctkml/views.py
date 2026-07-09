from django.shortcuts import render

def index(request):
    return render(request, 'gctkml/index.html')