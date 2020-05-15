import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from icecreamapp.models import Variety
from ..connection import Connection

def variety_form(request):
    if request.method == 'GET':
        template = 'variety/variety_form.html'
        context = {
            
        }

        return render(request, template, context)