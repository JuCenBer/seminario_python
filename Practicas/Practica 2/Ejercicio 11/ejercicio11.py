from ast import comprehension
import os

estudiantes = {}

ruta = os.path.join(os.path.dirname(os.path.realpath(".")),
                    "Practica 2", "Ejercicio 11")

archivo_eval1 = open(os.path.join(ruta, "eval1.txt"), 'r', encoding="UTF-8")
archivo_eval2 = open(os.path.join(ruta, "eval2.txt"), "r", encoding="UTF-8")

archivo_nombres2 = open(os.path.join(
    ruta, "nombres_2.txt"), "r", encoding="UTF-8")
archivo_nombres1 = open(os.path.join(
    ruta, "nombres_1.txt"), "r", encoding="UTF-8")

nombres1 = archivo_nombres1.read().replace(
    "\n", "").replace("'", "").split(",")
nombres2 = archivo_nombres2.read().replace(
    "\n", "").replace("'", "").split(",")

notas1 = archivo_eval1.read().replace("\n", "").replace(" ", "").split(",")
notas2 = archivo_eval2.read().replace("\n", "").replace(" ", "").split(",")

nombres_coincidentes = list({nombre.lower().strip(" ")
                             for nombre in nombres1 if nombre in nombres2})
print('Los nombres coincidentes entre ambas listas son: ')
for nombre in range(len(nombres_coincidentes)):
    aux = list(nombres_coincidentes[nombre])
    aux[0] = aux[0].upper()
    aux = "".join(aux)
    print(aux)

for estudiante in range(len(nombres1)):
    estudiantes[nombres1[estudiante]] = (
        (int(notas1[estudiante])), int(notas2[estudiante]))

nombres = list(estudiantes.keys())
print('   Nombre\tEval1 \t Eval2 \t Total')
print()
for estudiante in range(len(estudiantes)):
    total = int(estudiantes[nombres[estudiante]][0]) + \
        int(estudiantes[nombres[estudiante]][1])
    print(
        f'{estudiante}  {nombres[estudiante]:<10}{estudiantes[nombres[estudiante]][0]:>8}{estudiantes[nombres[estudiante]][1]:>8}{total:>8}')
