"""L'ereditarietà è una delle tre regole fondamentali della programmazioni orientata agli oggetti. 
L'ereditarietà nasce dall'idea di creare classi collegata tra di loro. 
Infatti le classi non necessariamente devono essere indipendenti tra di loro, 
ma pensare che possano essere l'una il caso più specifico di un'altra.
Una sottoclasse è una specializzazione della descrizione di una classe, detta la sua superclasse,
della quale essa mutua parte degli attributi e i metodi.
Alcuni metodi dell'ereditarietà in python sono:

super(): Questa funzione è usata per richiamare il costruttore della
superclasse, permettendo alla sottoclasse di estendere o modificare il
comportamento della superclasse. super() è usata anche per accedere a metodi
della superclasse che sono stati sovrascritti nella sottoclasse.

Sovrascrittura di metodi: La sottoclasse può sovrascrivere i metodi della
superclasse per modificare o estendere il loro comportamento. Questo è utile
quando si vuole che una sottoclasse si comporti in modo leggermente diverso
rispetto alla superclasse.

Ereditarietà Multipla: Python supporta l'ereditarietà multipla, permettendo
a una classe di ereditare da più classi base. Questo può essere realizzato
elencando le superclasses tra parentesi durante la definizione della
sottoclasse
"""
class Veicolo:
    def __init__(self, marca, modello, anno):
        self.marca = marca
        self.modello = modello
        self.anno = anno

    def descrizione(self):
        return f"{self.anno} {self.marca} {self.modello}"

    def avvia(self):
        print("Il veicolo è stato avviato.")

class Auto(Veicolo):
    def __init__(self, marca, modello, anno, numero_porte):
        super().__init__(marca, modello, anno)
        self.numero_porte = numero_porte

    def descrizione(self):
        base_descrizione = super().descrizione()
        return f"{base_descrizione}, {self.numero_porte} porte"

    def suona_clacson(self):
        print("Beep beep!")

class Moto(Veicolo):
    def __init__(self, marca, modello, anno, tipo):
        super().__init__(marca, modello, anno)
        self.tipo = tipo

    def descrizione(self):
        base_descrizione = super().descrizione()
        return f"{base_descrizione}, tipo: {self.tipo}"

    def impennata(self):
        print("Guarda, sto impennando!")

# Esempio di utilizzo
auto1 = Auto("Toyota", "Corolla", 2020, 4)
moto1 = Moto("Yamaha", "MT-07", 2019, "Sportiva")

print(auto1.descrizione())  # Output: 2020 Toyota Corolla, 4 porte
auto1.avvia()               # Output: Il veicolo è stato avviato.
auto1.suona_clacson()       # Output: Beep beep!

print(moto1.descrizione())  # Output: 2019 Yamaha MT-07, tipo: Sportiva
moto1.avvia()               # Output: Il veicolo è stato avviato.
moto1.impennata()           # Output: Guarda, sto impennando!
