import pandas as pd
import numpy as np

def carica_e_esplora_dataset(file_path):
    df = pd.read_csv(file_path)
    colonne = ['ID_Cliente', 'Età', 'Durata_Abbonamento', 'Tariffa_Mensile', 
                          'Dati_Consumati', 'Servizio_Clienti_Contatti', 'Churn']
    df = df[colonne]  # Filtra solo le colonne necessarie
    
    print("Prime righe del dataset:")
    print(df.head(), "\n")
    print("Informazioni generali sul dataset:")
    print(df.info(), "\n")
    print("Statistiche descrittive del dataset:")
    print(df.describe(), "\n")
    
    if 'Churn' in df.columns:
        print("Distribuzione dei valori nella colonna 'Churn':")
        print(df['Churn'].value_counts(), "\n")
    else:
        print("La colonna 'Churn' non è presente nel dataset.\n")
    
    print("Valori mancanti per colonna:")
    print(df.isnull().sum(), "\n")
    
    return df

def pulizia_dati(df):
    df = df.dropna()
    
    # rimuovere righe con età negative
    df = df[df['Età'] >= 0]
    
    # rimuovere righe con tariffe mensili irrealistiche
    df = df[(df['Tariffa_Mensile'] >= 0) & (df['Tariffa_Mensile'] <= 1000)]
    
    print("Informazioni generali sul dataset dopo la pulizia:")
    print(df.info(), "\n")
    print("Statistiche descrittive del dataset dopo la pulizia:")
    print(df.describe(), "\n")
    
    return df

def analisi_esplorativa_dati(df):
    # Analisi specifiche per le colonne desiderate
    if 'Churn' in df.columns:
        churn_group = df.groupby('Churn').agg({
            'Età': ['mean', 'median'],
            'Durata_Abbonamento': ['mean', 'median'],
            'Tariffa_Mensile': ['mean', 'median'],
            'Servizio_Clienti_Contatti': ['mean', 'median']
        })
        print("Relazioni tra Età, Durata Abbonamento, Tariffa Mensile, Servizio Clienti Contatti e Churn:")
        print(churn_group, "\n")
    
    print("Correlazioni tra le variabili:")
    print(df.corr(), "\n")
    
    return df

def preparazione_dati_per_modellazione(df):
    if 'Churn' in df.columns:
        df['Churn'] = df['Churn'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    df[numeric_columns] = (df[numeric_columns] - df[numeric_columns].mean()) / df[numeric_columns].std()
    
    print("Dati dopo la preparazione per la modellazione:")
    print(df.head(), "\n")
    
    return df

def main(file_path):
    df = None
    while True:
        print("\nMenu:")
        print("1. Carica ed esplora il dataset")
        print("2. Pulisci i dati")
        print("3. Esegui analisi esplorativa dei dati")
        print("4. Prepara i dati per la modellazione")
        print("5. Esci")
        
        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            df = carica_e_esplora_dataset(file_path)
        elif scelta == '2':
            if df is not None:
                df = pulizia_dati(df)
            else:
                print("Carica prima il dataset.")
        elif scelta == '3':
            if df is not None:
                df = analisi_esplorativa_dati(df)
            else:
                print("Carica e pulisci prima il dataset.")
        elif scelta == '4':
            if df is not None:
                df = preparazione_dati_per_modellazione(df)
            else:
                print("Carica, pulisci ed esplora prima il dataset.")
        elif scelta == '5':
            print("Uscita in corso...")
            break
        else:
            print("Opzione non valida. Riprova.")

# Esempio di utilizzo della funzione main
if __name__ == "__main__":
    file_path = 'giovedi18/clienti_telecomunicazioni.csv'
    main(file_path)
