from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def index(request):
    return render(request, 'tycole/index.html')


def printing(request):
    return render(request, 'tycole/printing.html')