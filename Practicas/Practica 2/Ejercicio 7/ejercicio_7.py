from operator import truediv
import string
from collections import Counter

palabra = input("Ingrese la palabra o frase a evaluar: ")
cont = Counter()
for caracter in palabra:
    if caracter in string.ascii_letters:  # Como solo tengo que evaluar los letras que se repitan, me fijo si el caracter es una letra
        cont[caracter] += 1

es_heterograma = False
for i in cont:
    if cont[i] != 1:
        es_heterograma = True

if es_heterograma:
    print(f"La palabra {palabra} es un heterograma")
else:
    print(f"La palabra {palabra} no es un heterograma")
