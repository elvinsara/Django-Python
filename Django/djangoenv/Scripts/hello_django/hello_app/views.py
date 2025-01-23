from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def print_hello(request):
    #return HttpResponse("<h1>Hello Django</h1>")
    movie_details = {'title': 'Titanic','year':2000}
    return render(request,'index.html',movie_details)
