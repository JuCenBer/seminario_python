tabla = {"A E I O U L N R S T": 1, "D G": 2, "B C M P": 3,
         "F H V W Y": 4, "K": 5, "J X": 8, "Q Z": 10}

palabra = input("Ingrese la palabra a evaluar: ").upper()
puntaje = 0

for letra in palabra:
    for clave in tabla:
        if letra in clave:
            puntaje += tabla[clave]
            # Para que no recorra el resto de claves una vez encontrada la letra.
            break

print(f"El puntaje de la palabra {palabra} es: {puntaje}")
