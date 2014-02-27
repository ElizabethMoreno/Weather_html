# coding: utf-8
import json
import requests
import webbrowser
from jinja2 import Template

def direccion_viento (direccion):
	for grados in str(direccion):
		if direccion >= 337.5 and direccion < 22.5:
			return "N"
		elif direccion >= 22.5 and direccion < 67.5:
			return "NE"
		elif direccion >= 67.5 and direccion < 112.5:
			return "E"
		elif direccion >= 112.5 and direccion < 157.5:
			return "SE"
		elif direccion >= 157.5 and direccion < 202.5:
			return "S"
		elif direccion >= 202.5 and direccion < 247.5:
			return "SO"
		elif direccion >= 247.5 and direccion < 292.5:
			return "O"
		elif direccion >= 292.5 and direccion < 337.5:
			return "NO"

provincias = {"1":"Almeria","2":"Cadiz","3":"Cordoba","4":"Granada","5":"Huelva","6":"Jaen","7":"Malaga","8":"Sevilla"}
provincia = provincias.keys()
plantilla = open('Plantilla weather.html','r')
resultado = open('resultado.html','w')
html = ''

ciudad = []
temp_minima = []
temp_maxima = []
viento = []
direccionviento = []

for provincia in provincias:
	respuesta = requests.get('http://api.openweathermap.org/data/2.5/weather',params = {'q': '%s,spain' %provincia})
	ciudad.append(provincias[provincia])
	dicc = json.loads(respuesta.text)
	temp_minima.append(int(dicc["main"]["temp_min"] - 273))
	temp_maxima.append(int(dicc["main"]["temp_max"] - 273))
	viento.append(int(dicc["wind"]["speed"] * 1.61))
	direccionviento.append(direccion_viento(dicc["wind"]["deg"]))

for linea in plantilla:
	html += linea
print html
miplantilla = Template(html)
salida = miplantilla.render(provincias = 'provincia',temp_min = 'temp_minima',temp_max = 'temp_maxima',vel_viento = 'viento',direc_viento = 'direccionviento')

resultado.write('miplantilla')
webbrowser.open("resultado.html")