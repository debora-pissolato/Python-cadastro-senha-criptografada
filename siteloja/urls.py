from django.urls import path
from .views import cadCli
 
urlpatterns = [
    path('', cadCli, name='formcli'),
]
 