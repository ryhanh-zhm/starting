from django.shortcuts import render
from django.http import HttpResponse

def index_view(request):
    return HttpResponse('<h1> This is HOME page! </h1>')

def about_view(request):
    return HttpResponse('<h1> About Us: </h1>')

def contact_view(request):
    return HttpResponse('<h1> Contact with us: </h1>')