import csv
import os


ruta_archivo = os.path.abspath("netflix_titles.csv")

archivo = open(ruta_archivo, "r", encoding="utf-8")
reader = csv.reader(archivo, delimiter=',')
cabecera = next(reader)
datos = list(reader)
paises = set()

for show in datos:
    paises.update(filter(lambda pais: (pais != None), map(lambda pais: pais.strip(" ") if pais !=
                  '' else None, show[5].split(","))))

paises = list(paises)
paises.sort()
print(paises)
