import csv
import os
from telnetlib import NOP


def tipos_shows_pais(pais, datos):
    tipos_shows = set()
    for show in datos:
        if (pais in show[5]):
            tipos_shows.update(
                map(lambda genero: genero.strip(" "), show[10].split(',')))
    for tipo in tipos_shows:
        print(tipo)


def paises_existentes(datos):
    paises = set()
    for show in datos:
        paises.update(map(lambda pais: pais.strip(" ") if pais !=
                      '' else None, show[5].split(',')))
    print(paises)


def pais_en_show(pais, show):
    if(pais in show[5]):
        print('El pais esta en el show')
    else:
        print('El pais no esta en el show')


ruta_archivo = os.path.abspath("netflix_titles.csv")

archivo = open(ruta_archivo, "r", encoding="utf-8")
reader = csv.reader(archivo, delimiter=',')
cabecera = next(reader)
datos = list(reader)
print('Ingrese un pais: ')
pais = ''
# tipos_shows_pais(input(pais), datos[:])
paises_existentes(datos[:])

print('Ingrese el show a analizar')
show = ''
input(show)
for linea in datos:
    if(show in linea[2]):
        show = linea
        break
print('Ingrese un pais: ')
pais = ''
pais_en_show(input(pais), show)
