from django.urls import path
from . import views # need to import views in order to use 


urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("phal", views.phal, name="phal")

]
