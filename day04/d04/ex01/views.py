from django.shortcuts import render
import requests

def django(request):
    return render(request, 'ex01/django.html')
def display(request):
    return render(request, 'ex01/display.html')
def templates(request):
    return render(request, 'ex01/template.html')