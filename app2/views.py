from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Ram(request):
    return HttpResponse('<h1>chocolate boy</h2>')
