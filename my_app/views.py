
from django.shortcuts import render, redirect
from django.views.generic import View
from django.http import HttpResponse
from .models import *

# Create your views here.

def home(request):
    return render(request, "index.html")
