import csv

# Classe che rappresenta un'auto
class Auto:
    def __init__(self, marca, modello, prezzo):
        self._marca = marca
        self._modello = modello
        self._prezzo = prezzo
    
    # Getter
    def get_marca(self):
        return self._marca
    
    def get_modello(self):
        return self._modello
    
    def get_prezzo(self):
        return self._prezzo
    
    # Setter
    def set_marca(self, marca):
        self._marca = marca
    
    def set_modello(self, modello):
        self._modello = modello
    
    def set_prezzo(self, prezzo):
        if prezzo < 0:
            raise ValueError("Il prezzo non può essere negativo.")
        self._prezzo = prezzo

# Funzione per leggere le auto da un file CSV
def leggi_auto_da_csv(filename):
    lista_auto = []
    try:
        with open(filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                auto = Auto(row['Marca'], row['Modello'], int(row['Prezzo']))
                lista_auto.append(auto)
    except FileNotFoundError:
        print(f"Errore: Il file {filename} non è stato trovato.")
    return lista_auto

# Funzione per salvare le auto in un file CSV
def salva_auto_su_csv(lista_auto, filename):
    try:
        with open(filename, mode='w', newline='') as file:
            fieldnames = ['Marca', 'Modello', 'Prezzo']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for auto in lista_auto:
                writer.writerow({
                    'Marca': auto.get_marca(),
                    'Modello': auto.get_modello(),
                    'Prezzo': auto.get_prezzo()
                })
    except Exception as e:
        print(f"Errore durante il salvataggio: {e}")

# Funzione per aggiungere un'auto alla lista
def aggiungi_auto(lista_auto, marca, modello, prezzo):
    try:
        auto = Auto(marca, modello, prezzo)
        lista_auto.append(auto)
    except ValueError as e:
        print(f"Errore: {e}")

# Funzione per rimuovere un'auto dalla lista
def rimuovi_auto(lista_auto, marca, modello):
    auto_trovata = False
    for auto in lista_auto:
        if auto.get_marca() == marca and auto.get_modello() == modello:
            lista_auto.remove(auto)
            auto_trovata = True
            break
    if not auto_trovata:
        print("Errore: Auto non trovata.")

# Funzione per visualizzare tutte le auto
def visualizza_auto(lista_auto):
    for auto in lista_auto:
        print(f"Marca: {auto.get_marca()}, Modello: {auto.get_modello()}, Prezzo: {auto.get_prezzo()}")

# main per far girare il programma
def main():
    filename = "concessionario.csv"
    lista_auto = leggi_auto_da_csv(filename)

    while True:
        print("\nMenu:")
        print("1. Visualizza tutte le auto")
        print("2. Aggiungi un'auto")
        print("3. Rimuovi un'auto")
        print("4. Salva e esci")

        scelta = input("Scegli un'opzione: ")
        
        if scelta == '1':
            visualizza_auto(lista_auto)
        elif scelta == '2':
            marca = input("Inserisci la marca: ")
            modello = input("Inserisci il modello: ")
            prezzo = int(input("Inserisci il prezzo: "))
            aggiungi_auto(lista_auto, marca, modello, prezzo)
        elif scelta == '3':
            marca = input("Inserisci la marca: ")
            modello = input("Inserisci il modello: ")
            rimuovi_auto(lista_auto, marca, modello)
        elif scelta == '4':
            salva_auto_su_csv(lista_auto, filename)
            print("Dati salvati. Uscita dal programma.")
            break
        else:
            print("Opzione non valida, riprova.")

# Esecuzione del programma principale
if __name__ == "__main__":
    main()
