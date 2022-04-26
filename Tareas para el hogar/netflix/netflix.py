from base64 import decode
import csv
import os

archivo1 = open(os.path.join(
    os.getcwd(), "netflix", "netflix_titles.csv"), 'r', encoding="UTF-8")
archivo2 = open(os.path.join(os.getcwd(), "netflix",
                "nuevoarchivo.csv"), "w", encoding="UTF-8")

csvreader = csv.reader(archivo1, delimiter=',')
csvwriter = csv.writer(archivo2)

csvwriter.writerow(next(csvreader))


csvwriter.writerows(filter(lambda titulo: titulo[7] == '2021', csvreader))

archivo1.close()
archivo2.close()
