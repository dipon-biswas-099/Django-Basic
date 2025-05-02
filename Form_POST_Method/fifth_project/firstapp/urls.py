from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name ="homepage"),
    path('form/',views.submit_form, name = "submit_form" ),
    
]