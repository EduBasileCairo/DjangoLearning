from django.http import HttpResponse
def saludo(request):
    return HttpResponse("<html><body><h1>Hola mundo MA</h1></body></html>""Hola mundo MA")

# PARÁMETROS EN LA URL:
# Es frecuente cuando se trabaja con sitios WEB dinámicos tener la necesidad de pasar parámetros a la URL. Vamos a ver cómo manejar contenido dinámico y pasar parámetros de la URL con Django. Vamos a realizar un script que muestre la hora y día del sistema. Para crear contenido dinámico: Creamos una nueva vista:

from django.http import HttpResponse
import datetime
#Definición de la vista:
def saludo(request):
    texto = """
    <html>
    <body>
    <h1>Hola mundo 5</h1>
    </body>
    </html>
    """
    return HttpResponse(texto)

#Definición de una vista para contenido dinámico
def fecha(request):
    miFecha=datetime.datetime.now()
    fecha_hora_formateada = miFecha.strftime("%Y-%m-%d %H:%M:%S")
    texto2 = f"""<html>
    <body>
    <h2>Fecha y hora actual: {fecha_hora_formateada} </h2> 
    </body>
    </html>
    """
#% miFecha
    return HttpResponse(texto2)

# Vamos a realizar otro ejemplo. Crearemos un script que calcule la edad que tendremos en un año determinado. En este ejemplo usaremos paso de parámetros por URL. Creamos la vista:
def calcEdad(request, year):
    try:
        year = int(year)  # Convierte el año a entero
        edadActual = 18  # Edad actual (puedes cambiarla)
        edadFutura = edadActual + (year - datetime.datetime.now().year)  # Calcula la edad futura

        if edadFutura < 0:
            mensaje = f"No has nacido aún. ¡Viaja al pasado!"
        elif year < datetime.datetime.now().year:
             mensaje = f"Ese año ya pasó. ¡Viaja al futuro!"
        else:
            mensaje = f"En el año {year} tendrás {edadFutura} años."

        documento = f"""
        <html>
        <body>
        <h2>{mensaje}</h2>
        </body>
        </html>
        """
        return HttpResponse(documento)

    except ValueError:
        return HttpResponse("Año no válido. Debe ser un número entero.")
    
    # Para visualizar levantar el servidor en la consola CMD con:
    # python manage.py runserver
    # En el navegador escribir la siguiente URL:
    # http://127.0.0.1:8000/edad/2050/
    # Si querés cambiar el año con la tecla retroceso se cambia el año y se pone / al final del nuevo año.