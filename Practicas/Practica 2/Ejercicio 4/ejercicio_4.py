evaluar = """ título: Experiences in Developing a Distributed Agent-based Modeling Toolkit
with Python
resumen: Distributed agent-based modeling (ABM) on high-performance computing resources
provides the promise of capturing unprecedented details of large-scale complex systems.
However, the specialized knowledge required for developing such ABMs creates barriers to
wider adoption and utilization. Here we present our experiences in developing an initial
implementation of Repast4Py, a Python-based distributed ABM toolkit. We build on our
experiences in developing ABM toolkits, including Repast for High Performance Computing
(Repast HPC), to identify the key elements of a useful distributed ABM toolkit. We leverage
the Numba, NumPy, and PyTorch packages and the Python C-API to create a scalable modeling
system that can exploit the largest HPC resources and emerging computing architectures.""".lower().split("resumen: ")

titulo = evaluar[0].replace(" título: ", "").split()
print(titulo)
resumen = evaluar[1].split(".")
especificaciones = {"titulo": "", "facil": 0,
                    "aceptable": 0, "dificil": 0, "muy_dificil": 0}

if len(titulo) <= 10:
    especificaciones["titulo"] = "titulo ok"
else:
    especificaciones["titulo"] = "titulo mal"

for oracion in resumen:
    sum = 0
    for palabra in oracion.split():
        sum += 1
    print(sum)
    if (sum <= 12):
        especificaciones["facil"] += 1
    elif(sum <= 17):
        especificaciones["aceptable"] += 1
    elif (sum <= 25):
        especificaciones["dificil"] += 1
    else:
        especificaciones["muy_dificil"] += 1

print("Resumen de la evaluacion del articulo: \nTitulo:{}\nCantidad de oraciones faciles: {}\nCantidad de oraciones aceptables: {}\nCantidad de oraciones dificiles: {}\nCantidad de oraciones muy dificiles: {}".format(
    especificaciones["titulo"], especificaciones["facil"], especificaciones["aceptable"], especificaciones["dificil"], especificaciones["muy_dificil"]))
