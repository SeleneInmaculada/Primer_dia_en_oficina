"""
Solución simple al problema de maximización del poder del ejército.
Recursos: 1200 comida, 800 madera, 600 oro.
Unidades: Espadachín (60 comida, 20 madera, 0 oro, 70 poder),
Arquero (80 comida, 10 madera, 40 oro, 95 poder),
Jinete (140 comida, 0 madera, 100 oro, 230 poder).
"""

# Solución óptima calculada analíticamente
espadachines = 6
arqueros = 0
jinetes = 6

# Cálculo del poder total
poder_total = espadachines * 70 + arqueros * 95 + jinetes * 230

# Verificación de recursos
comida_usada = espadachines * 60 + arqueros * 80 + jinetes * 140
madera_usada = espadachines * 20 + arqueros * 10 + jinetes * 0
oro_usado = espadachines * 0 + arqueros * 40 + jinetes * 100

print("Solución óptima para maximizar el poder del ejército:")
print(f"Espadachines: {espadachines}")
print(f"Arqueros: {arqueros}")
print(f"Jinetes: {jinetes}")
print(f"Poder total: {poder_total}")
print(f"Recursos usados:")
print(f"  Comida: {comida_usada}/1200")
print(f"  Madera: {madera_usada}/800")
print(f"  Oro: {oro_usado}/600")