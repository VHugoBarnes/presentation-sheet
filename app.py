# coding: utf-8
import pdfkit
from jinja2 import Environment, FileSystemLoader
import util


env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("template.html")


# Verifica si el archivo user.json ya contiene los datos del usuario.
# Si el no contiene datos pasa al método para la configuración inicial.
if util.has_data():
    print("El archivo contiene datos")
    # Pasa a preguntar los datos para la hoja de presentación
    usuario = util.take_data()
else:
    util.configuration()
    usuario = util.take_data()
    

# usuario = {
#     'tema': 'Unidad 6. Núcleo',
#     'nombre': 'Víctor Hugo Vázquez Gómez',
#     'asignatura': 'Sistemas Operativos',
#     'carrera': 'INGENIERÍA EN SISTEMAS COMPUTACIONALES',
#     'profesor': 'Keko Kaka',
#     'fecha': '30 diciembre 2019'
# }

html = template.render(usuario)

options = {
    'page-size': 'Letter',
    'margin-top': '0.1in',
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
    'dpi': 100,
    'page-height': 279,
    'page-width': 216,
    'quiet': ''
}

pdfkit.from_string(html, 'hoja_presentacion.pdf', options=options)

print("La hoja de presentación se ha generado con éxito")
print("El pdf tiene el nombre de hoja_presentacion.pdf")