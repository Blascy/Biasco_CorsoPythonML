class Veicolo:
    def __init__(self,marca,modello,anno):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno
        self.__accensione = False #non necessario metterlo in parentesi

    def accendi(self):
        scelta1 = input("La macchina è spenta, vuoi accenderla? (si/no): ")

        if scelta1.lower() == 'si':
            self.__accensione = True #usare self.__accensione per riferirsi correttamente all'attributo privato della classe.
            print("Hai acceso la macchina")
        elif scelta1.lower() == 'no':
            self.__accensione = False
            print("Continuerà a rimanere spenta")
        else:
            print("Errore")

    def spegni(self):
        if self.__accensione:
            self.__accensione = False
            print("Hai spento la macchina")
        else:
            print("la macchina è gia spenta")
            
    def stato_accensione(self):
        return f"Stato accensione: {'accesa' if self.__accensione else 'spenta'}"


class Auto(Veicolo):
    def __init__(self,marca,modello,anno,__numero_porte):
        super().__init__(marca,modello,anno)
        self.__numero_porte = __numero_porte

    def suona_clacson(self):
        print("suona clacson")

class Furgone(Veicolo):
    def __init__(self,marca,modello,anno,__capacita_carico):
        super().__init__(marca,modello,anno)
        self.__capacita_carico = __capacita_carico

    def carica(self):
        print(f"Il Furgone da {self.__capacita_carico} kg è stato caricato")

    def scarica(self):
        print(f"Il Furgone da {self.__capacita_carico} kg è stato caricato")

class Motocicletta(Veicolo):
    def __init__(self,marca,modello,anno,__tipo):
        super().__init__(marca,modello,anno)
        self.__tipo = __tipo

    def esegui_wheelie(self):
        scelta2 = input("Di che tipo è la tua auto?(sportivo/utilitaria/touring/ecc): ")
        if scelta2.lower() == 'sportivo' or 'sportiva':
            print(f"Esegui wheelie con la tua moto {scelta2}")
        else:
            print(f"Non puoi eseguire wheelie con la tua moto {scelta2}")

class GestoreParcoVeicoli(Veicolo,Auto,Furgone,Motocicletta):





"""senza GestoreParcoVeicoli funziona
veicolo1 = Veicolo('furgone volkwswagen','passat',2001)
veicolo1.accendi()
veicolo1.spegni()
print(veicolo1.stato_accensione())

auto1 = Auto('audi','rs6',2022,'due')
auto1.suona_clacson()

furgone1 = Furgone('Iveco','baggy',2000,100)
furgone1.carica()
furgone1.scarica()

moto1 = Motocicletta('yamaha','pegaso',2012,'sportiva')
moto1.esegui_wheelie()
"""