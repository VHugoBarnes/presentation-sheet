# coding: utf-8
import json
from datetime import datetime
import os


filepath = os.path.dirname(os.path.abspath(__file__))


def configuration():
    """
        Este método se utiliza la primera vez que se inicia el programa.
        Recolecta los datos que siempre se repiten en una hoja de presentación.
    """
    print("Ingresa tu nombre:", end=" ")
    nombre = input()
    print("Ingresa tu carrera:", end=" ")
    carrera = input()

    # Se guardan los datos como un dict (o como JSON)
    data = {
        "nombre": nombre,
        "carrera": carrera
    }

    # se abre en modo escritura ("w") el archivo user.json
    # y con el método dump de json se escribe en el archivo
    with open(filepath + "/user.json", "w") as outfile:
        json.dump(data, outfile)
    

def has_data():
    """
        Este método se asegura de que haya algún dato en el 
        archivo user.json
        En caso de que el archivo contenga un dato devolverá True.
    """
    if os.path.getsize(filepath + "/user.json") > 0:
        return True
    else:
        return False


def take_data():
    """
        Devuelve un diccionario con los datos necesarios para imprimir
        la hoja de presentación.
    """

    # Preguntamos si es uno o más estudiantes
    print("Ingresa la cantidad de estudiantes (de 1 a 5, contandote):", end=" ")
    cantidad_estudiante = int(input())

    if(cantidad_estudiante <= 0 or cantidad_estudiante > 5):
        raise Exception("Ingresa un número del 1 al 5, por favor")

    # Preguntamos todos los datos...
    print("Tema:", end=" ")
    tema = input()

    students_arr = []

    if(cantidad_estudiante >= 2 and cantidad_estudiante <= 5):
        for x in range(cantidad_estudiante):
            i = input("Nombre del estudiante #" + str(x+1) + ":")
            students_arr.append(i)
    
    print("Asignatura:", end=" ")
    asignatura = input()
    print("Profesor:", end=" ")
    profesor = input()
    print("¿Fecha de hoy? (y/n)", end=" ")
    res = input().lower()

    # ¿Fecha de hoy o de otro día?
    if res == "y":
        fecha = fecha_actual(datetime.now())
    else:
        print("Fecha:", end=" ")
        fecha = input()

    # Abre user.json para leer los datos del usuario.
    with open(filepath + "/user.json", "r") as json_file:
        data = json.load(json_file)

        if(cantidad_estudiante >= 2 and cantidad_estudiante <= 5):
            nombre = students_arr
        else:
            nombre = [data["nombre"]]
        
        datos = {
            "tema": tema,
            "nombre": nombre,
            "asignatura": asignatura, 
            "carrera": data["carrera"],
            "profesor": profesor,
            "fecha": fecha
        }

    return datos

def fecha_actual(date):
    """
        Este método devuelve un mensaje personalizado de la fecha.
    """
    months = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", 
              "agosto", "septiembre", "octubre", "noviembre", "diciembre")

    day = date.day

    month = months[date.month - 1]
    
    year = date.year

    message = "{} de {} del {}".format(day, month, year)

    return message
