from django.urls import path
from . import views

app = 'portfolio'

urlpatterns = [
    path('', views.home, name='home'),
]   
