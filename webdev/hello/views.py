from django.http import HttpResponse
from django.shortcuts import render




# Create your views here.
def index(request): # request argument
    return render(request, "hello/index.html") #HttpResponse("hello, mom")  # need to import httpResponse 


def phal(request):
    return HttpResponse("hello, phal")

def greet(request, name):
    return render(request, "hello/greet.html", {
      "name": name.capitalize()  
    })
        
        #HttpResponse(f"hello {name.capitalize()}, welcome") # add f, to tell its a format string