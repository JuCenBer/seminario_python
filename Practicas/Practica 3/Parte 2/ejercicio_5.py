import datetime
import csv
import os
from time import strptime

with open(os.path.abspath("BBB_nuevo.csv"), encoding="utf-8") as logs:
    reader = csv.reader(logs, delimiter=',')
    cabecera = next(reader)
    lista_logs = list(reader)

dias_semana = ['lunes', 'martes', 'miercoles',
               'jueves', 'viernes', 'sabado', 'domingo']
formato = "%d/%m/%Y %H:%M"

primera_fecha = datetime.datetime.strptime(lista_logs[0][0], formato)
print(primera_fecha)
for linea in lista_logs:
    ultima_fecha = datetime.datetime.strptime(linea[0], formato)

diferencia = (primera_fecha - ultima_fecha).days
print(diferencia)
