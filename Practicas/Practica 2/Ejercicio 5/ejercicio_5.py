frase = """Tres tristes tigres, tragaban trigo en un trigal, en tres tristes trastos, tragaban
trigo tres tristes tigres.""".replace(",", "").replace(".", "").lower().split()

palabra = input("Ingrese una palabra: ").lower()
sum = 0

for word in frase:
    if(palabra == word):
        sum += 1

print(f"Resultado: {sum}")
