from django.urls import path

from . import views  # import local directory

urlpatterns = [
    path("", views.index, name="index")
    
]
