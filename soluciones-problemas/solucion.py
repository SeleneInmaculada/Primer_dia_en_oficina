"""
Solución al problema de maximización del poder del ejército con recursos limitados.
Ahora usando datos de la carpeta archive para calcular el máximo poder (fuerza total).
"""

import csv

max_poder = 0
max_row = None

with open('archive/belligerents.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            poder = int(row['str'])
            if poder > max_poder:
                max_poder = poder
                max_row = row
        except ValueError:
            pass

print(f"El máximo poder (fuerza total) en los datos de archive es: {max_poder}")
print("Detalles del ejército más poderoso:")
print(f"Nombre: {max_row['nam']}")
print(f"Comandante: {max_row['co']}")
print(f"Fuerza inicial: {max_row['intst']}")
print(f"Bajas: {max_row['cas']}")
print(f"Caballería: {max_row['cav']}")
print(f"Artillería: {max_row['arty']}")
print(f"Actores: {max_row['actors']}")
print(f"Número de batalla: {max_row['isqno']}")