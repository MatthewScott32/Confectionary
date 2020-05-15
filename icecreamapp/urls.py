from django.urls import path
from .views import *

app_name = "icecreamapp"

urlpatterns = [
     path('', variety_list, name='variety_list'),
]
