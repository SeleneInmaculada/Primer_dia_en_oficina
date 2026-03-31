"""
Solución al problema de maximización del poder del ejército con recursos limitados.
Ahora usando datos de la carpeta archive para calcular el máximo poder (fuerza total).
Genera un archivo HTML con tabla y gráfico.
"""

import csv

max_poder = 0
max_row = None

with open('../archive/belligerents.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            poder = int(row['str'])
            if poder > max_poder:
                max_poder = poder
                max_row = row
        except ValueError:
            pass

# Datos para el HTML
nombre = max_row['nam']
comandante = max_row['co']
str_total = int(max_row['str'])
cav = int(max_row.get('cav', 0))
arty = int(max_row.get('arty', 0))
infanteria = str_total - cav - arty
actores = max_row['actors']
batalla = max_row['isqno']

# Generar HTML
html_content = f"""
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Máximo Poder del Ejército</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        body {{ font-family: Arial, sans-serif; margin: 20px; }}
        table {{ border-collapse: collapse; width: 100%; }}
        th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
        th {{ background-color: #f2f2f2; }}
        canvas {{ max-width: 400px; margin: 20px 0; }}
    </style>
</head>
<body>
    <h1>Máximo Poder del Ejército en los Datos de Archive</h1>
    <p>El máximo poder (fuerza total) es: <strong>{max_poder}</strong> soldados.</p>
    
    <h2>Detalles del Ejército Más Poderoso</h2>
    <table>
        <tr><th>Campo</th><th>Valor</th></tr>
        <tr><td>Nombre</td><td>{nombre}</td></tr>
        <tr><td>Comandante</td><td>{comandante}</td></tr>
        <tr><td>Fuerza Total</td><td>{str_total}</td></tr>
        <tr><td>Caballería</td><td>{cav}</td></tr>
        <tr><td>Artillería</td><td>{arty}</td></tr>
        <tr><td>Infantería (estimada)</td><td>{infanteria}</td></tr>
        <tr><td>Actores</td><td>{actores}</td></tr>
        <tr><td>Número de Batalla</td><td>{batalla}</td></tr>
    </table>
    
    <h2>Composición del Ejército</h2>
    <canvas id="armyChart"></canvas>
    
    <script>
        const ctx = document.getElementById('armyChart').getContext('2d');
        const armyChart = new Chart(ctx, {{
            type: 'pie',
            data: {{
                labels: ['Infantería', 'Caballería', 'Artillería'],
                datasets: [{{
                    data: [{infanteria}, {cav}, {arty}],
                    backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56'],
                }}]
            }},
            options: {{
                responsive: true,
            }}
        }});
    </script>
</body>
</html>
"""

# Guardar el HTML
with open('solucion_visual.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Archivo HTML generado: solucion_visual.html")
print("Ábrelo en un navegador para ver la tabla y el gráfico.")