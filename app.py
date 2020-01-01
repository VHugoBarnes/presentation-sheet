# coding: utf-8
import pdfkit
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("template.html")

usuario = {
    'tema': 'Unidad 6. Núcleo',
    'nombre': 'Víctor Hugo Vázquez Gómez',
    'asignatura': 'Sistemas Operativos',
    'carrera': 'INGENIERÍA EN SISTEMAS COMPUTACIONALES',
    'profesor': 'Keko Kaka',
    'fecha': '30 diciembre 2019'
}

html = template.render(usuario)

options = {
    'page-size': 'Letter',
    'margin-top': '0.1in',
    'margin-right': '0.1in',
    'margin-bottom': '0.1in',
    'margin-left': '0.1in',
    'dpi': 100,
    'page-height': 279,
    'page-width': 216
}

pdfkit.from_string(html, 'hoja_presentacion.pdf', options=options)