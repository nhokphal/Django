from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.


class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:  # looking at inside the session, if there isnt any list, will add session task
        request.session["tasks"] = []
    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid(): #if form completed as required
            task = form.cleaned_data["task"] # create new variable 
            request.session["tasks"] += [task] # adding incre tasks value from old value if have any    
            return HttpResponseRedirect(reverse("tasks:index")) # return to index task after done 
        else:
            return render(request, "tasks/add.html",
            {
                "form": form
            })
    return render(request, "tasks/add.html", {
        "form": NewTaskForm() 

    })