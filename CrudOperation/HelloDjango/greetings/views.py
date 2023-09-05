from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return render(request, 'welcome.html')

def greet(request, username):
    return render(request, 'greet.html', {'username': username})

def farewell(request, username):
    return render(request, 'farewell.html', {'username': username})
