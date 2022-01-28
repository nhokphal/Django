from django.shortcuts import render
import datetime
# Create your views here.


def index(request):
    now = datetime.datetime.now() # defince a new variable for current date 
    return render(request, "newyear/index.html", {
        "newyear": now.month == 1 and now.day == 1
    })