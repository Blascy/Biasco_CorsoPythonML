class Animale:
    def __init__(self):
        self.nome = input("Inserisci nome dell'animale: ")
        self.eta = int(input("Inserisci età dell'animale: "))

    def fai_suono(self):
        inserisci_suono = input("Che suono fa questo animale? ")


class Leone(Animale):
    def __init__(self):
        super().__init__()
        self.luogo_caccia = input(f"Inserisci in che luogo caccia {self.nome}: ")

    def mostra_luogo_caccia(self):
        print(f"Il luogo di caccia del leone è {self.luogo_caccia}")


class Giraffa(Animale):
    def __init__(self):
        super().__init__()
        self.cosa_non_mangia = input(f"Cosa non mangia {self.nome}?: ")

    def mostra_cosa_non_mangia(self):
        print(f"La giraffa non mangia {self.cosa_non_mangia}")


class Pinguino(Animale):
    def __init__(self):
        super().__init__()
        self.habitat = input(f"Dove vivono i {self.nome}? Fa caldo o freddo?: ")

    def mostra_habitat(self):
        print(f"I pinguini vivono in un habitat che è {self.habitat}")


# Esempi di utilizzo delle classi

# Creazione di un animale generico e chiamata del metodo fai_suono
animale_generico = Animale()
animale_generico.fai_suono()

# Creazione di istanze specifiche di Leone, Giraffa e Pinguino
leone = Leone()
giraffa = Giraffa()
pinguino = Pinguino()

# Chiamata ai metodi specifici delle sottoclassi
leone.mostra_luogo_caccia()
giraffa.mostra_cosa_non_mangia()
pinguino.mostra_habitat()
