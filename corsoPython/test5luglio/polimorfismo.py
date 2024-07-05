"""Il polimorfismo è un concetto fondamentale nella programmazione orientata agli oggetti (OOP) che permette di 
trattare oggetti di classi diverse tramite un'interfaccia comune. 
In Python, il polimorfismo si manifesta principalmente attraverso la sovrascrittura dei metodi (overriding). 
Python non supporta l'overloading dei metodi nel senso tradizionale presente in altri linguaggi di programmazione, 
ma si possono ottenere risultati simili utilizzando argomenti predefiniti e variadici.

Sovrascrittura dei Metodi (Overriding). 
La sovrascrittura dei metodi avviene quando una sottoclasse 
fornisce una specifica implementazione di un metodo già definito nella sua superclasse. 
Questo permette di specializzare il comportamento di un metodo in base alla sottoclasse che lo implementa.

Overloading dei Metodi
L'overloading dei metodi, ovvero la possibilità di avere più metodi nella stessa classe con lo stesso nome 
ma parametri differenti, non è supportato direttamente in Python come in altri linguaggi. 
Tuttavia, è possibile simulare l'overloading utilizzando argomenti opzionali o variadici.
"""
class Animale:
    def emetti_suono(self):
        return "Questo è un suono generico di un animale."

class Cane(Animale):
    def emetti_suono(self):
        return "Bau bau!"

class Gatto(Animale):
    def emetti_suono(self):
        return "Miao miao!"

class Mucca(Animale):
    def emetti_suono(self):
        return "Muu muu!"

# Funzione che utilizza il polimorfismo
def fai_emettere_suono(animali):
    for animale in animali:
        print(animale.emetti_suono())

# Creazione degli oggetti
cane = Cane()
gatto = Gatto()
mucca = Mucca()

# Lista di animali
animali = [cane, gatto, mucca]

# Uso del polimorfismo
fai_emettere_suono(animali)
