import csv

file_path = "giovedi27\studenti.csv"

def leggi_file(file_path):
    # Legge il file CSV e ritorna un dizionario con gli studenti e i loro voti
    database = {}
    with open('file_path','r') as file:
        reader = csv.reader(file)
        for row in file:
            nome = row[0]
            voti = list(map(int, row[1:]))  # Converte le stringhe in interi
            database[nome] = voti
    return database

def scrivi_file(file_path,database):
    #scrivi il database nel file csv
    with open('file_path','w', newline= '') as file:
        writer = csv.writer(file)
        for nome,voti in database.item():
            writer.writerow([nome] + voti)

def mostra_studenti(database):
    # Mostra l'elenco degli studenti con i loro voti e la media
    for nome,voti in database.item():
        media = sum(voti)/len(voti) if voti else 0
        print(f"Nome:{nome}, Voti:{voto}, Media:{media:.2f}")
        # :Inizia la specifica di formattazione 
        # .2: Indica che il numero deve essere visualizzato con 2 cifre decimali.
        #f: Indica che il numero è un numero a virgola mobile (float).
    else:
        print("Studente {nome} non trovato")

def elimina_studenti(database):
    #elimina uno studente dal database
    nome = input("Inserisci il nome dello studente da eliminare: ")
    if nome in database:
        del database[nome]
        print(f"Elimina lo studente: {nome}")
    else:
        print(f"Nessuno studente di nome: {nome} da eliminare")

def menu():
    database = leggi_file(file_path)
    while True:
        print("\nMenu:")
        print("1. Mostra elenco alunni e voti")
        print("2. Aggiungi alunno")
        print("3. Cerca alunno")
        print("4. Elimina alunno")
        print("5. Esci")
        scelta = input("Scegli un'opzione: ")

        if scelta == '1':
            mostra_studenti(database)
        elif scelta == '2':
            aggiungi_studente(database)
            scrivi_file(file_path, database)
        elif scelta == '3':
            cerca_studente(database)
        elif scelta == '4':
            elimina_studente(database)
            scrivi_file(file_path, database)
        elif scelta == '5':
            break
        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    menu()



