"""Create un classe libro che ha al suo interno:
-titolo;
- autore;
- prezzo;
- codice isbn viene generato automaticamente in maniera randomica ogni volta che inserito un libro;
- stato_prestito;

Metodo

Create poi 2 metodi:
- Metodo sconto per applicare lo sconto della percentuale passata al prezzo;
- Metodo prestito per cambiare lo stato del prestito, quindi se è libero diventa prestato, se è prestato diventa libero"""
import random

class Libro:
    def __init__(self, titolo, autore, prezzo, stato_prestito='libero'): #isbn è statico non si passa
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo
        self.codice_isbn = self.genera_codice_isbn()
        self.stato_prestito = stato_prestito

    def genera_codice_isbn(self):
        # Genera un codice ISBN randomico
        return str(random.randint(1000000000000, 9999999999999))

    def applica_sconto(self, percentuale):
        # Applica uno sconto al prezzo
        if 0 <= percentuale <= 100:
            sconto = self.prezzo * (percentuale / 100)
            self.prezzo -= sconto
        else:
            print("Percentuale di sconto non valida.")

    def cambia_stato_prestito(self):
        # Cambia lo stato del prestito
        if self.stato_prestito == 'libero':
            self.stato_prestito = 'prestato'
        elif self.stato_prestito == 'prestato':
            self.stato_prestito = 'libero'
        else:
            print("Stato di prestito non valido.")

    def visualizza(self):
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Prezzo: {self.prezzo}, Codice ISBN: {self.codice_isbn}, Stato Prestito: {self.stato_prestito}"

# Esempio di utilizzo
libro = Libro("Il nome della rosa", "Umberto Eco", 20.0)
print(libro.visualizza())

# Applicare uno sconto del 10%
libro.applica_sconto(10)
print(libro.visualizza())

# Cambiare stato prestito
libro.cambia_stato_prestito()
print(libro.visualizza())

# Cambiare di nuovo stato prestito
libro.cambia_stato_prestito()
print(libro.visualizza())
