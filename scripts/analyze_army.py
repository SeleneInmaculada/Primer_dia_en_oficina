import csv

max_str = 0
max_row = None

with open('archive/belligerents.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        try:
            str_val = int(row['str'])
            if str_val > max_str:
                max_str = str_val
                max_row = row
        except ValueError:
            pass

print(f"El ejército más grande tiene {max_str} soldados.")
print(f"Detalles: {max_row}")