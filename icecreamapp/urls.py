from django.urls import path
from .views import *
from django.urls import path

app_name = "icecreamapp"

urlpatterns = [
     path('', variety_list, name='variety_list'),
     path('variety/form', variety_form, name='variety_form'),
     # path('variety/<int:variety_id>/', variety_details, name='variety'),
]
