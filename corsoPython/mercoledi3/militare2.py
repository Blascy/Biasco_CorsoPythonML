class UnitaMilitare:
    def __init__(self, nome, numero_soldati):
        self.nome = nome
        self.numero_soldati = numero_soldati

    def muovi(self):
        print(f"L'unità {self.nome} si è mossa")

    def attacca(self):
        print(f"L'unità {self.nome} attacca")

    def ritira(self):
        print(f"L'unità {self.nome} si ritira")

    def mostra_dettagli(self):
        print(f"Nome: {self.nome}, Numero di soldati: {self.numero_soldati}")


class Fanteria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, costruisci_trincea):
        super().__init__(nome, numero_soldati)
        self.costruisci_trincea = costruisci_trincea

    def mostra_dettagli(self):
        super().mostra_dettagli()
        print(f"Costruisce trincea: {self.costruisci_trincea}")


class Artiglieria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, calibra_artiglieria):
        super().__init__(nome, numero_soldati)
        self.calibra_artiglieria = calibra_artiglieria

    def mostra_dettagli(self):
        super().mostra_dettagli()
        print(f"Calibra artiglieria: {self.calibra_artiglieria}")


class Cavalleria(UnitaMilitare):
    def __init__(self, nome, numero_soldati, cavalleria):
        super().__init__(nome, numero_soldati)
        self.cavalleria = cavalleria

    def mostra_dettagli(self):
        super().mostra_dettagli()
        print(f"Cavalleria: {self.cavalleria}")


class SupportoLogistico(UnitaMilitare):
    def __init__(self, nome, numero_soldati, rifornisci_unita):
        super().__init__(nome, numero_soldati)
        self.rifornisci_unita = rifornisci_unita

    def mostra_dettagli(self):
        super().mostra_dettagli()
        print(f"Rifornisce unità: {self.rifornisci_unita}")


class Ricognizione(UnitaMilitare):
    def __init__(self, nome, numero_soldati, conduci_ricognizione):
        super().__init__(nome, numero_soldati)
        self.conduci_ricognizione = conduci_ricognizione

    def mostra_dettagli(self):
        super().mostra_dettagli()
        print(f"Conduce ricognizione: {self.conduci_ricognizione}")


class ControlloMilitare:
    def __init__(self):
        self.unita_registrate = {}  # Registro delle unità militari

    def registra_unita(self):
        while True:
            scelta = input('Vuoi aggiungere un\'unità al registro? (si/no): ').strip().lower()
            if scelta == 'si':
                tipo_unita = input("Tipo di unità (Fanteria/Artiglieria/Cavalleria/SupportoLogistico/Ricognizione): ").strip()
                nome = input("Nome dell'unità: ").strip()
                numero_soldati = int(input("Numero di soldati: ").strip())
                
                if tipo_unita.lower() == 'fanteria':
                    costruisci_trincea = input("Costruisce trincea (True/False): ").strip().lower() == 'true'
                    unita = Fanteria(nome, numero_soldati, costruisci_trincea)
                elif tipo_unita.lower() == 'artiglieria':
                    calibra_artiglieria = input("Calibra artiglieria (True/False): ").strip().lower() == 'true'
                    unita = Artiglieria(nome, numero_soldati, calibra_artiglieria)
                elif tipo_unita.lower() == 'cavalleria':
                    cavalleria = input("Cavalleria (True/False): ").strip().lower() == 'true'
                    unita = Cavalleria(nome, numero_soldati, cavalleria)
                elif tipo_unita.lower() == 'supportologistico':
                    rifornisci_unita = input("Rifornisce unità (True/False): ").strip().lower() == 'true'
                    unita = SupportoLogistico(nome, numero_soldati, rifornisci_unita)
                elif tipo_unita.lower() == 'ricognizione':
                    conduci_ricognizione = input("Conduce ricognizione (True/False): ").strip().lower() == 'true'
                    unita = Ricognizione(nome, numero_soldati, conduci_ricognizione)
                else:
                    print("Tipo di unità non valido")
                    continue
                
                if nome in self.unita_registrate:
                    print("Unità militare già presente")
                else:
                    self.unita_registrate[nome] = unita
                    print(f"Unità {nome} aggiunta al registro")
            elif scelta == 'no':
                print("Arrivederci")
                break
            else:
                print("Errore: scelta non valida")
                
        print("Unità registrate:", list(self.unita_registrate.keys()))

    def mostra_unita(self):
        if not self.unita_registrate:
            print("Nessuna unità registrata presente")
        else:
            print("Le unità registrate sono:")
            for unita in self.unita_registrate.values():
                unita.mostra_dettagli()
                print()  # Per separare i dettagli delle unità

    def dettagli_unita(self):
        self.mostra_unita()

# Esempio di utilizzo
controllo = ControlloMilitare()
controllo.registra_unita()
controllo.dettagli_unita()