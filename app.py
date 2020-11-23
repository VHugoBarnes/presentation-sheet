# coding: utf-8
import pdfkit
from jinja2 import Environment, FileSystemLoader
import util
import time
import os


path = os.path.dirname(os.path.abspath(__file__))


env = Environment(loader=FileSystemLoader(path + "/templates"))
template = env.get_template("new-template.html")


# Verifica si el archivo user.json ya contiene los datos del usuario.
# Si el no contiene datos pasa al método para la configuración inicial.
if util.has_data():
    # Pasa a preguntar los datos para la hoja de presentación
    usuario = util.take_data()
else:
    util.configuration()
    usuario = util.take_data()
    print("Tu nombre y carrera se han guardado.")

# Almacena el string con el html
html = template.render(usuario)
css = './templates/styles.css'

options = {
    'page-size': 'Letter',
    'margin-top': '0in',
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0in',
    'page-height': 279,
    'page-width': 216,
    'quiet': '' # Para que no se muestre en consola los prints de wkhtmltopdf.
}

print("Generando PDF...")

pdfkit.from_string(html, path + '/hoja_presentacion.pdf', options=options, css=css)

print("La hoja de presentación se ha generado con éxito.")
print("El pdf se guardó en " + path + "/hoja_presentacion.pdf.")