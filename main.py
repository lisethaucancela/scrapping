from scraping import obtener_datos_todas_paginas
from procesamiento import procesar_datos, escribir_datos_csv, estadisticas_precio

def main():
    base_url = "https://www.fybeca.com/ofertas/dermo-days/"
    productos = obtener_datos_todas_paginas(base_url)
    datos_procesados = procesar_datos(productos)
    
    archivo_csv = "productos.csv"
    df = escribir_datos_csv(datos_procesados, archivo_csv)
    
    estadisticas_precio(df)

if __name__ == "__main__":
    main()
       