import os

estudiantes = {}

ruta = os.path.join(os.path.dirname(os.path.realpath(".")),
                    "Practica 2", "Ejercicio 10")

archivo_eval1 = open(os.path.join(ruta, "eval1.txt"), 'r', encoding="UTF-8")
archivo_eval2 = open(os.path.join(ruta, "eval2.txt"), "r", encoding="UTF-8")
archivo_nombres1 = open(os.path.join(
    ruta, "nombres_1.txt"), "r", encoding="UTF-8")

nombres1 = archivo_nombres1.read().replace(
    "\n", "").replace("'", "").split(",")

notas1 = archivo_eval1.read().replace("\n", "").replace(" ", "").split(",")
notas2 = archivo_eval2.read().replace("\n", "").replace(" ", "").split(",")
total = 0
for estudiante in range(len(nombres1)):
    estudiantes[nombres1[estudiante]] = int(
        notas1[estudiante]) + int(notas2[estudiante])
    total += estudiantes[nombres1[estudiante]]

prom = total/len(nombres1)
print(f'La nota promedio del total de notas es: {prom}')
print('Los alumnos que obtuvieron una nota total menor al promedio son: ')
nombres = list(estudiantes.keys())
print('   Nombre\tNota')
for estudiante in range(len(estudiantes)):
    if(estudiantes[nombres[estudiante]] < prom):
        print(
            f'{estudiante}  {nombres[estudiante]}\t{estudiantes[nombres[estudiante]]:<10}')
