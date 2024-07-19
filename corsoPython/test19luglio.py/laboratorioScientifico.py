"""Esercizio su Numpy

Scenario: Un laboratorio scientifico registra le temperature ogni ora.
Obiettivo: Utilizzare numpy per calcolare la temperatura media, minima e massima registrata.
Dati: Un array numpy di temperature registrate in una giornata.

Compiti:
Crea una dataset di dati da almeno 24 posizioni
Calcola la temperatura media 
Trova la temperatura massima e minima.
Determina la temperatura più probabile per le prossime 4 posizioni rispetto a un aumento costante di 0,2 gradi al giorno ogni settimana. 
"""

import numpy as np

# creo array di temperature registrate ogni ora in una giornata
np.random.seed(0)  # Impostiamo un seme per la ripetibilità
temperature_data = np.random.uniform(low=15, high=25, size=24)

print("Dataset di temperature (°C):")
print(temperature_data)

# calcolo la temperatura media
mean_temperature = np.mean(temperature_data)
print(f"Temperatura media: {mean_temperature:.2f} °C")

# calcolo la temperatura massima e minima
max_temperature = np.max(temperature_data)
min_temperature = np.min(temperature_data)
print(f"Temperatura massima: {max_temperature:.2f} °C")
print(f"Temperatura minima: {min_temperature:.2f} °C")

#aumento costante di 0,2 gradi al giorno
increment_per_day = 0.2
hours = 4
ultima_temperatura = temperature_data[-1]  # Ultima temperatura registrata

# Calcoliamo la temperatura prevista per le prossime 4 ore
future_temperatures = [ultima_temperatura + i * increment_per_day for i in range(1, hours + 1)]
print("Temperature previste per le prossime 4 ore:")
print(future_temperatures)
