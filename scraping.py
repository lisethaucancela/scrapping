
import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def obtener_datos_producto(url):
    respuesta = requests.get(url)
    soup = BeautifulSoup(respuesta.text, "html.parser")
    productos = []
    
    #Adaptar los selectores a la estructura del sitio
    items = soup.select(".product-tile")
    for item in items:
        name_element = item.select_one(".pdp-link a")
        price_element = item.select_one(".value")
        
        if(name_element and price_element):
            name =name_element.get_text(strip=True)
            price = price_element.get_text(strip=True)
            productos.append((name, price)) 
        else:
            continue
        
    return productos

#Obtener datos de todas las paginas

def obtener_datos_todas_paginas(base_url):
    productos=[]
    start = 0  
    while True:
        url=F"{base_url}/?start={start}&sz=18&maxsize=18"
        nuevo_productos = obtener_datos_producto(url) 
        if not nuevo_productos:  # Si no hay más productos, salir del bucle
            break 
        productos.extend(nuevo_productos)
        start +=18
    return productos
        