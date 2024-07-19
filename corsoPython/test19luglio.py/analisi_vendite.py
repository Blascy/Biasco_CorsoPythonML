import pandas as pd

# Lettura del file CSV
df = pd.read_csv('performance_giornaliera.csv')

# Calcolo delle vendite medie per ora lavorativa
df['Vendite per Ora Lavorativa'] = df['Vendite'] / df['Ore Lavorative']

# Identificazione dei giorni con la massima e la minima vendite per ora lavorativa
giorno_max = df.loc[df['Vendite per Ora Lavorativa'].idxmax()]
giorno_min = df.loc[df['Vendite per Ora Lavorativa'].idxmin()]

print("Giorno con la massima vendite per ora lavorativa:")
print(giorno_max)

print("\nGiorno con la minima vendite per ora lavorativa:")
print(giorno_min)

# Salvataggio dei risultati su file CSV
df.to_csv('performance_giornaliera_analizzata.csv', index=False)

# Creazione di DataFrame per i giorni con massima e minima efficienza
giorno_max_df = pd.DataFrame([giorno_max])
giorno_min_df = pd.DataFrame([giorno_min])

# Salvataggio dei giorni con la massima e minima efficienza su file CSV
giorno_max_df.to_csv('giorno_max_efficienza.csv', index=False)
giorno_min_df.to_csv('giorno_min_efficienza.csv', index=False)
