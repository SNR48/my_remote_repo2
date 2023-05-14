from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def display_view(request):
    return HttpResponse('<h2>Welcome to the django with new laptop</h2>')