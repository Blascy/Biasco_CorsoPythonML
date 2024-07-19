import pandas as pd

# Lettura del file CSV
df = pd.read_csv('test19luglio.py\vendite.csv')

# Raggruppamento dei dati per "Data" e "Filiale" e calcolo della somma delle vendite
df_raggruppato = df.groupby(['Data', 'Filiale']).agg({'Vendite': 'sum'}).reset_index()

# Calcolo delle vendite medie giornaliere per filiale
vendite_medie_per_filiale = df_raggruppato.groupby('Filiale').agg({'Vendite': 'mean'}).reset_index()
vendite_medie_per_filiale.rename(columns={'Vendite': 'Vendite Medie Giornaliere'}, inplace=True)

print("Vendite medie giornaliere per filiale:")
print(vendite_medie_per_filiale)

# Determinazione della filiale con le vendite medie giornaliere più alte
filiale_top = vendite_medie_per_filiale.loc[vendite_medie_per_filiale['Vendite Medie Giornaliere'].idxmax()]
print(f"\nFiliale con le vendite medie giornaliere più alte:")
print(filiale_top)

# Salvataggio dei risultati su file CSV
vendite_medie_per_filiale.to_csv('vendite_medie_per_filiale.csv', index=False)
filiale_top_df = pd.DataFrame([filiale_top])
filiale_top_df.to_csv('filiale_con_vendite_piu_alte.csv', index=False)
