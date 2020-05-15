import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from icecreamapp.models import Variety, Flavor, VarietyFlavor
from ..connection import Connection

def variety_detail(request, variety_id):
    if request.method == "GET":
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = create_variety
            db_cursor = conn.cursor()
            
            db_cursor.execute("""
        select  v.id v_id
                v.name,
                v.country_of_origin,
                f.id f_id,
                f.name fname,
                f.alcohol_percent,
                vf.toppings,
                vf.id variety_flavor_id
                from icecreamapp_variety v 
                left join icecreamapp_varietyflavor vf on vf.variety_id = v.id
                left join icecreamapp_flavor f on vf.flavor_id = f.id
            WHERE v.id = ?
            """, (variety_id,))

        return db_cursor.fetchone()
    
    def create_variety(cursor, row):
        row = sqlite3.Row(cursor, row)

        variety = Variety()
        variety.id = row["id"]
        variety.name = row["name"]
        variety.country_of_origin = row['country_of_origin']

        variety.all_flavors = list()

        flavor = Flavor()
        flavor.id = row['flavor_id']
        flavor.name = row['flavor_name']
        flavor.alcohol_percent = row['alcohol_percent']
        flavor.toppings = row["toppings"]
        flavor.variety_flavor_id = row["variety_flavor_id"]

    

    
    
        return (variety,flavor,)