import string

texto = """The constants defined in this module are:The constants defined in,
this module are:

string.ascii_letters
The concatenation of the ascii_lowercase and ascii_uppercase constants,
described below. This value is not locale-dependent.

string.ascii_lowercase
The lowercase letters 'abcdefghijklmnopqrstuvwxyz'. This value is not,
locale-dependent and will not change.

string.ascii_uppercase
The uppercase letters 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'. This value is not,
locale-dependent and will not change.""".lower().split()


while True:
    letra = input("Ingrese una letra: ")
    if(letra in string.ascii_letters):
        break
    else:
        print('No ingreso una letra.')

conjunto = set()

for palabra in texto:
    if(palabra.startswith(letra)):
        conjunto.add(palabra)

print(conjunto)
