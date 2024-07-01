class Biblioteca:
    def __init__(self):
        self.titolo = ""
        self.autore = ""
        self.pagine = 0

    def creaLibro(self):
        self.titolo = input("Inserisci il titolo del libro: ")
        self.autore = input("Inserisci l'autore del libro: ")
        self.pagine = int(input("Inserisci il numero di pagine del libro: "))

    def descrizione(self):
        print(f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine")


token = True
biblioteca1 = Biblioteca()
while token:
    biblioteca1.creaLibro()
    biblioteca1.descrizione()
    scelta = input("Vuoi inserire altri libri? (sì/no): ")
    if scelta.lower() == "no":
        token = False
    else:
        token = True

     

    