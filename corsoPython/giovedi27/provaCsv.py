import csv

# Percorso del file CSV
file_path = "giovedi27/studenti.csv"

# Apri il file CSV
with open(file_path, 'r') as file:
    # Crea un oggetto reader
    reader = csv.reader(file)

    # Itera sulle righe del file
    for row in reader:
        nome = row[0]
        voti = list(map(int, row[1:]))  # Converte le stringhe in interi
        print(f"Nome: {nome}, Voti: {voti}")
