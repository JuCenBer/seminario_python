import csv
import os


def informar(show, ano):
    ano = str(ano)
    if(ano in show[7]):
        print(show[2] + ", " + show[7])


ruta_archivo = os.path.abspath("netflix_titles.csv")

archivo = open(ruta_archivo, "r", encoding="utf-8")
reader = csv.reader(archivo, delimiter=',')
cabecera = next(reader)
datos = list(reader)

print('Ingrese el año')
anio = input()
for linea in datos:
    informar(linea, anio)
