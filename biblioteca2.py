class Libro:
    def __init__(self, titolo, autore, isbn):
        self.titolo = titolo
        self.autore = autore
        self.isbn = isbn

    def descrizione(self):
        print(f"Il libro '{self.titolo}' con autore {self.autore}, ha codice ISBN {self.isbn}")

class Libreria:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        if libro.titolo not in [lib.titolo for lib in self.catalogo]:
            self.catalogo.append(libro)
            print(f"Il libro '{libro.titolo}' è stato aggiunto al catalogo")
        else:
            print("Libro già presente nel catalogo")

    def mostra_catalogo(self):
        if self.catalogo:
            print("Catalogo della libreria:")
            for libro in self.catalogo:
                libro.descrizione()
        else:
            print("Il catalogo è vuoto")

# Creazione della libreria
mia_libreria = Libreria()

# Creazione dei libri e aggiunta al catalogo
titolo1 = input("Inserisci il titolo del primo libro: ")
autore1 = input("Inserisci l'autore del primo libro: ")
isbn1 = input("Inserisci l'ISBN del primo libro: ")
libro1 = Libro(titolo1, autore1, isbn1)
mia_libreria.aggiungi_libro(libro1)

# Mostra il catalogo
mia_libreria.mostra_catalogo()

# Aggiunta di un altro libro
titolo2 = input("Inserisci il titolo del secondo libro: ")
autore2 = input("Inserisci l'autore del secondo libro: ")
isbn2 = input("Inserisci l'ISBN del secondo libro: ")
libro2 = Libro(titolo2, autore2, isbn2)
mia_libreria.aggiungi_libro(libro2)

# Mostra il catalogo aggiornato
mia_libreria.mostra_catalogo()

