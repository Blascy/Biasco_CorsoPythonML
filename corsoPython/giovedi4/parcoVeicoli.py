class Veicolo:
    def __init__(self, marca, modello, anno):
        self.__marca = marca
        self.__modello = modello
        self.__anno = anno

    def get_marca(self):
        return self.__marca

    def get_modello(self):
        return self.__modello

    def get_anno(self):
        return self.__anno

    def calcola_tassa(self):
        return 0  # Implementazione di default, può essere sovrascritta nelle sottoclassi

    def mostra_dettagli(self):
        print(f"Marca: {self.get_marca()}, Modello: {self.get_modello()}, Anno: {self.get_anno()}")


class Automobile(Veicolo):
    def __init__(self, marca, modello, anno, cilindrata, potenza):
        super().__init__(marca, modello, anno)
        self.__cilindrata = cilindrata
        self.__potenza = potenza

    def get_cilindrata(self):
        return self.__cilindrata

    def get_potenza(self):
        return self.__potenza

    def calcola_tassa(self):
        if self.__potenza > 185:
            return self.__potenza * 20
        else:
            return self.__cilindrata * 0.1


class Motocicletta(Veicolo):
    def __init__(self, marca, modello, anno, potenza):
        super().__init__(marca, modello, anno)
        self.__potenza = potenza

    def get_potenza(self):
        return self.__potenza

    def calcola_tassa(self):
        return self.__potenza * 0.05


class Bicicletta(Veicolo):
    def calcola_tassa(self):
        return 25.0


class Monopattino(Veicolo):
    def calcola_tassa(self):
        return 15.0


class GestoreParco:
    def __init__(self):
        self.veicoli = []

    def aggiungi_veicolo(self, veicolo):
        self.veicoli.append(veicolo)

    def mostra_veicoli(self):
        for veicolo in self.veicoli:
            veicolo.mostra_dettagli()
            print(f"Tassa: {veicolo.calcola_tassa()}€\n")

    def calcola_tassa_totale(self):
        return sum(veicolo.calcola_tassa() for veicolo in self.veicoli)

# Esempio di utilizzo
gestore = GestoreParco()

auto1 = Automobile("Fiat", "Punto", 2015, 1400, 100)
auto2 = Automobile("Ferrari", "488", 2020, 3902, 670)
moto = Motocicletta("Yamaha", "R1", 2018, 200)
bici = Bicicletta("Bianchi", "Pista", 2020)
monopattino = Monopattino("Xiaomi", "Mi Electric Scooter", 2021)

gestore.aggiungi_veicolo(auto1)
gestore.aggiungi_veicolo(auto2)
gestore.aggiungi_veicolo(moto)
gestore.aggiungi_veicolo(bici)
gestore.aggiungi_veicolo(monopattino)

gestore.mostra_veicoli()
print(f"Tassa totale: {gestore.calcola_tassa_totale()}€")
