import sqlite3
from django.shortcuts import render, redirect, reverse
from icecreamapp.models import Variety
from ..connection import Connection

def variety_list(request):
    if request.method == 'GET':
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row

            db_cursor = conn.cursor()
            db_cursor.execute("""
            select
                v.id,
                v.name,
                v.country_of_origin
            FROM icecreamapp_variety v
            ORDER BY v.name
            """)

            all_varieties = []
            dataset = db_cursor.fetchall()
            
            for row in dataset:
                variety = Variety()
                variety.id = row['id']
                variety.name = row['name']
                variety.country_of_origin = row['country_of_origin']
                
                all_varieties.append(variety)

        template = 'variety/variety_list.html'
        context = {
            'all_varieties': all_varieties
        }

        return render(request, template, context)