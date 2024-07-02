class Vendita:
    def __init__(self):
        self.importi = []

    def inserisci_importi(self):
        while True:
            scelta_importo = input("Inserisci importi di vendita (o 'stop' per terminare): ")
            if scelta_importo.lower() == 'stop':
                break
    
            try:
                importo = float(scelta_importo)  # Converte l'input in un numero
                self.importi.append(importo)  # Aggiunge l'importo alla lista
                print(f"Importo aggiunto: {importo} euro")
            except ValueError:
                print("Input non valido. Per favore inserisci un numero.")

        print(f"Lista completa degli importi: {self.importi}")

    def calcolo_totale(self):
        if len(self.importi) == 0:
            print("Non sono presenti dati di vendita")
        else:
            totale = sum(self.importi)
            media = sum(self.importi)/len(self.importi)
            print(f"Il totale degli importi è: {totale} euro mentre la media è: {media}" )


# Esempio di utilizzo della classe Vendita
vendita = Vendita()
vendita.inserisci_importi()
vendita.calcolo_totale()

#mancano queste due
'''Vendite Sopra la Media: Trova e stampa una lista di tutti i giorni in cui le vendite hanno superato 
la media delle vendite di tutto il periodo. 
Assicurati di gestire correttamente il caso in cui non ci siano vendite sopra la media.

Visualizzazione dei Risultati: Per ogni punto sopra, stampa i risultati in modo chiaro e leggibile, 
con messaggi appropriati che spiegano cosa sta mostrando il programma.'''