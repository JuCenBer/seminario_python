import datetime
import csv
from collections import Counter
import os

with open(os.path.abspath("BBB_nuevo.csv"), encoding="utf-8") as logs:
    reader = csv.reader(logs, delimiter=',')
    cabecera = next(reader)
    lista_logs = list(reader)

dias_semana = ['lunes', 'martes', 'miercoles',
               'jueves', 'viernes', 'sabado', 'domingo']
formato = "%d/%m/%Y %H:%M"
contador = Counter()
for linea in lista_logs:
    print(dias_semana[datetime.datetime.strptime(linea[0], formato).weekday()])
    contador[dias_semana[datetime.datetime.strptime(
        linea[0], formato).weekday()]] += 1

for elemento in contador:
    print(f"{elemento}: {contador[elemento]}")
