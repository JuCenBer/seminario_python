import os

ruta = os.path.join(os.path.dirname(os.path.realpath(".")),
                    "Practica 2", "Ejercicio 10")

estudiantes = {}
archivo_eval1 = open(os.path.join(ruta, "eval1.txt"), 'r', encoding="UTF-8")
archivo_eval2 = open(os.path.join(ruta, "eval2.txt"), "r", encoding="UTF-8")
archivo_nombres1 = open(os.path.join(
    ruta, "nombres_1.txt"), "r", encoding="UTF-8")

nombres1 = archivo_nombres1.read().replace(
    "\n", "").replace("'", "").split(",")

notas1 = archivo_eval1.read().replace("\n", "").strip(" ").split(",")
notas2 = archivo_eval2.read().replace("\n", "").strip(" ").split(",")

total = 0
for estudiante in range(len(nombres1)):
    estudiantes[nombres1[estudiante]] = int(
        notas1[estudiante]) + int(notas2[estudiante])
    total += estudiantes[nombres1[estudiante]]

prom = total/len(nombres1)
print(f'La nota promedio del total de notas es: {prom}')
estudiantes_bajo_promedio = {}
for estudiante in estudiantes:
    if(estudiantes[estudiante] < prom):
        estudiantes_bajo_promedio[estudiante] = estudiantes[estudiante]

if(len(estudiantes_bajo_promedio) >= 1):
    print('Los alumnos que obtuvieron una nota total menor que el promedio total de notas son: ')
    i = 0
    print('   Nombre\tNota')
    for estudiante in estudiantes_bajo_promedio:
        print(
            f'{i}  {estudiante}\t{estudiantes[estudiante]:<10}')
        i += 1
else:
    print("Ningun estudiante tuvo una nota menor que el promedio total de notas.")

archivo_eval1.close()
archivo_eval2.close()
archivo_nombres1.close()
