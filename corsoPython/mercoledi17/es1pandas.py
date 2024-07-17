import pandas as pd

def stampa_menu():
    print("\nMenu:")
    print("1. Mostrare il dataframe")
    print("2. Visualizzare le prime e le ultime cinque righe del DataFrame.")
    print("3. Visualizzare il tipo di dati di ciascuna colonna.")
    print("4. Calcolare statistiche descrittive di base per le colonne numeriche (media, mediana, deviazione standard).")
    print("5. Identificare e rimuovere eventuali duplicati.")
    print("6. Gestire i valori mancanti sostituendoli con la mediana della rispettiva colonna.")
    print("7. Aggiungere una nuova colonna 'Categoria Età'.")
    print("8. Salvare il DataFrame pulito in un nuovo file CSV.")


# Creazione di un DataFrame con dati di esempio come un dizionario
data = {
    'Nome': ['Alice', 'Bob', 'Carla', 'Giovanni', 'Andrea', 'Laura'],
    'Età': [25, 30, 22, 34, 54, 20],
    'Città': ['Roma', 'Milano', 'Napoli', 'Molfetta', 'Palermo', 'Foggia'],
    'Salario': [30000, 25000, 17000, 20000, 80000, 75000]
}

df = pd.DataFrame(data)

def mostra_dataframe():
    # Stampa del DataFrame originale
    print("DataFrame Originale:")
    print(df)


def prime_ultime_cinque():
    prime_cinque = df.head()
    ultime_cinque = df.tail()
    print("\nMostra prime e ultime 5 righe del dataframe:")
    print(prime_cinque)
    print(ultime_cinque)


def tipo_colonna():
    # Visualizzare il tipo di dati di ciascuna colonna
    print("\nTipo di dati di ciascuna colonna:")
    print(df.dtypes)


def colonne_numeriche():
    colonne_num = df.select_dtypes(include='number')
    print("\nLa media delle colonne:")
    media = colonne_num.mean()
    print(media)

    print("\nLa mediana delle colonne:")
    mediana = colonne_num.median()
    print(mediana)

    print("\nLa deviazione standard delle colonne:")
    deviazione_standard = colonne_num.std()
    print(deviazione_standard)


def individua_rimuovi_duplicati():
    individua = df.duplicated()
    print("\nRighe duplicate individuate:")
    print(individua)

    rimuovi = df.drop_duplicates()
    print("\nDuplicati rimossi:")
    print(rimuovi)


def gestisci_valori_mancanti():
    # Calcola la mediana delle colonne numeriche
    mediana_età = df['Età'].median()
    mediana_salario = df['Salario'].median()
    
    # Sostituisci i valori mancanti con la mediana rispettiva
    df['Età'].fillna(mediana_età, inplace=True)
    df['Salario'].fillna(mediana_salario, inplace=True)
    
    print("\nDataFrame con Valori Mancanti Gestiti:")
    print(df)


def gestore_età():
    # Definizione delle categorie di età
    def categorizza_età(età):
        if età <= 18:
            return 'Giovane'
        elif età <= 65:
            return 'Adulto'
        else:
            return 'Senior'
    
    # Applica la funzione di categorizzazione alla colonna 'Età'
    df['Categoria Età'] = df['Età'].apply(categorizza_età)
    print("\nDataFrame con Colonna 'Categoria Età' Aggiunta:")
    print(df)


def salva_dataframe():
    # Salva il DataFrame in un nuovo file CSV
    nome_file = input("Inserisci il nome del file CSV per salvare il DataFrame: ").strip()
    df.to_csv(nome_file + '.csv', index=False)
    print(f"\nDataFrame salvato correttamente in '{nome_file}.csv'.")


def main():
    while True:  # Ciclo infinito per il menu interattivo
        stampa_menu()
        scelta = int(input("Scegli un opzione: "))
        
        if scelta == 1:
            mostra_dataframe()
        elif scelta == 2:
            prime_ultime_cinque()
        elif scelta == 3:
            tipo_colonna()
        elif scelta == 4:
            colonne_numeriche()
        elif scelta == 5:
            individua_rimuovi_duplicati()
        elif scelta == 6:
            gestisci_valori_mancanti()
        elif scelta == 7:
            gestore_età()
        elif scelta == 8:
            salva_dataframe()
        else:
            print("Opzione non valida, per favore scegline un'altra.")
        
        continua = input("\nVuoi continuare (sì/no)? ").strip().lower()
        if continua != 'sì' and continua != 'si':
            print("Uscita dal programma.")
            break


if __name__ == "__main__":
    main()
