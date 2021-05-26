from django.urls import path, include
from .views import *
 


app_name = "account"


urlpatterns = [
    path('', Home, name="index"),
    
]