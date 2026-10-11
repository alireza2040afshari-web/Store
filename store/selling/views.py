from django.shortcuts import render
from django.http import HttpResponse
import re

# Create your views here.
def homeView(request):
    return render(request , "store/home.html")