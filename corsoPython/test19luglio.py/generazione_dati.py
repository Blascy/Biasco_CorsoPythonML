import numpy as np
import pandas as pd

# seme per la ripetibilità
np.random.seed(0)

# Generazione delle date per 30 giorni
date = pd.date_range(start='2024-01-01', periods=30, freq='D')

# Generazione di dati casuali per Vendite e Ore Lavorative
vendite = np.random.uniform(low=1000, high=5000, size=len(date))
ore_lavorative = np.random.uniform(low=6, high=12, size=len(date))

# Creazione del DataFrame
df = pd.DataFrame({
    'Data': date,
    'Vendite': vendite,
    'Ore Lavorative': ore_lavorative
})

# Salvataggio del DataFrame su un file CSV
df.to_csv('performance_giornaliera.csv', index=False)

print("Dati generati e salvati in 'performance_giornaliera.csv'.")
