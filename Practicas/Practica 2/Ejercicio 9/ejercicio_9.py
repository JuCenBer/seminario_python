estructura = [
    '-*-*-',
    '--*--',
    '----*',
    '*----',
]

mapa = []


def verificacionCeldasAdyacente(celdas_fila, celda):
    tot = 0
    if (celda - 1 >= 0) and (celdas_fila[celda - 1] == '*'):
        tot += 1
    if(celda + 1 <= 4) and (celdas_fila[celda + 1] == '*'):
        tot += 1
    return tot


def verificacionFilaAdyacente(fila, celda):
    tot = 0
    celdas_fila = list(fila)
    if ((celdas_fila[celda]) == '*'):
        tot += 1
    tot += verificacionCeldasAdyacente(celdas_fila, celda)
    return tot


def armarMapa(mapa, fila_aux):
    mapa.append(''.join(fila_aux))


fila_aux = []
for fila in range(len(estructura)):
    celdas_fila = list(estructura[fila])
    fila_aux.clear()
    for celda in range(len(celdas_fila)):
        tot = 0
        if (celdas_fila[celda] == '-'):
            tot += verificacionCeldasAdyacente(celdas_fila, celda)
            if(fila - 1 >= 0):
                tot += verificacionFilaAdyacente(estructura[fila - 1], celda)
            if(fila + 1 <= 3):
                tot += verificacionFilaAdyacente(estructura[fila + 1], celda)
            fila_aux.append(str(tot))
        else:
            fila_aux.append('*')
    armarMapa(mapa, fila_aux)

for fila in mapa:
    print(fila)
