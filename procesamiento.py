import requests
from bs4 import BeautifulSoup
import time
import pandas as pd

def procesar_datos(productos):
    datos_procesados=[]  
    for nombre, precio in productos: 
        if precio.strip(): 
            precio = float(precio.replace("$","").replace("(Oferta)",""))
        else:
            precio = 0.0 
        datos_procesados.append({"Producto": nombre, "Precio": precio}) 
        
    return datos_procesados

def escribir_datos_archivo(datos, archivo):
    with open(archivo, "w", encoding="utf-8") as f:
        for linea in datos:
            f.write(linea + "\n")
    
    
def escribir_datos_csv(datos, archivo):
    df=pd.DataFrame(datos)
    df.to_csv(archivo, index=False,encoding="utf-8")
    return df

def estadisticas_precio(df):
    print(f"Precio promedio: ${df['Precio'].mean():.2f}")
    print(f"Precio maximo: ${df['Precio'].max():.2f}")   
    print(f"Precio minimo: ${df['Precio'].min():.2f}")      
    