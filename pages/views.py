# pages/views.py

from django.shortcuts import render
from django.http import HttpResponse

def home_page_view(request):
    """
    A simple view function that returns an HTTP response 
    containing the text 'Hello, World!'.
    """
    return HttpResponse("<h1>Hello, World! (Django)</h1>")