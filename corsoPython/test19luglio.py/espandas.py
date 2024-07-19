"""
Pandas è una libreria Python fondamentale per la manipolazione e l'analisi dei dati. Offre funzionalità che 
semplificano l'elaborazione dei dati strutturati. In particolare, offre strutture di dati e operazioni per 
manipolare tabelle numeriche e serie temporali. 

Pandas implementa due strutture dati fondamentali: DataFrame e Series.
DataFrame: Un DataFrame è una struttura dati bidimensionale simile a una tabella, con righe e colonne etichettate. 
È molto utile per l'analisi dei dati tabulari.
Es creazione:
"""
import pandas as pd

data = {
    'Nome': ['Alice', 'Bob', 'Charlie'],
    'Età': [25, 30, 35],
    'Città': ['Roma', 'Milano', 'Torino']
}
df = pd.DataFrame(data)
print(df)

"""
Series: Una Series è una struttura dati unidimensionale che può essere considerata come una colonna di un DataFrame.
Es Creazione:
"""
s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)

"""Es. Manipolazione:
Selezione e Indicizzazione"""

print(df['Nome'])
# Selezionare una riga per indice
print(df.iloc[1])

#filtraggio
filtered_df = df[df['Età'] > 30]
print(filtered_df)

#raggruppamento e aggregazione
grouped_df = df.groupby('Città').mean()
print(grouped_df)

#preprocessing dei dati, quindi pulizia e gestione dei dati mancanti
df_with_nan = df.copy()
df_with_nan.loc[1, 'Età'] = None
print(df_with_nan.fillna(df_with_nan['Età'].mean()))  # Riempie i valori mancanti con la media

#rinominare righe e colonne
df_renamed = df.rename(columns={'Nome': 'Nome Completo'})
print(df_renamed)

#analisi temporale
dates = pd.date_range(start='2024-01-01', periods=3)
df_dates = pd.DataFrame({'Data': dates, 'Valore': [100, 200, 300]})
print(df_dates)
