class Prodotto:
    def __init__(self):
        self.nome = input("Inserisci il nome del prodotto: ")
        self.costo_produzione = int(input("Inserisci il costo di produzione: "))
        self.prezzo_vendita = int(input("Inserisci il prezzo di vendita: "))

    def calcola_profitto(self):
        self.profitto = self.prezzo_vendita - self.costo_produzione
        if self.costo_produzione <= 0:
            print("Non può esserci profitto")
        else:
            print(f"Il profitto è di {self.profitto} euro")

class Elettronica(Prodotto):
    def __init__(self):
        super().__init__()
        self.garanzia = int(input("Inserisci garanzia del prodotto (in anni): "))

    def mostra_garanzia(self):
        if self.garanzia > 0:
            print(f"La garanzia del prodotto {self.nome} dal prezzo di {self.prezzo_vendita} euro è di {self.garanzia} anni")

class Abbigliamento(Prodotto):
    def __init__(self):
        super().__init__()
        self.materiale = input("Inserisci il materiale del capo di abbigliamento: ")

    def mostra_materiale(self):
        print(f"Il capo d'abbigliamento {self.nome} è prodotto con {self.materiale}")

class Fabbrica:
    def __init__(self):
        self.inventario = {}

    def aggiungi_prodotto(self):
        prodotto = Prodotto()
        if prodotto.nome not in self.inventario:
            self.inventario[prodotto.nome] = prodotto
            print(f"Il prodotto {prodotto.nome} è stato aggiunto all'inventario")
        else:
            print("Il prodotto è già presente nell'inventario")

    def mostra_inventario(self):
        if self.inventario:
            print("Inventario della fabbrica:")
            for nome, prodotto in self.inventario.items():
                print(f"- {nome}: {prodotto.prezzo_vendita} Euro (Costo Produzione {prodotto.costo_produzione} Euro)")
        else:
            print("L'inventario è vuoto")

    def vendi_prodotto(self):
        nome_prodotto = input("Inserisci il nome del prodotto da vendere: ")
        if nome_prodotto not in self.inventario:
            print("Nessun prodotto da rimuovere dall'inventario")
        else:
            prodotto = self.inventario[nome_prodotto]
            del self.inventario[nome_prodotto]
            profitto = prodotto.calcola_profitto()
            if profitto is not None:
                print(f"Il prodotto {nome_prodotto} è stato rimosso dall'inventario con profitto di {profitto} euro")
            else:
                print(f"Il prodotto {nome_prodotto} è stato rimosso dall'inventario")

#manca solo il metodo resi_prodotto


# Esempio di utilizzo delle classi
prodotto = Prodotto()
prodotto.calcola_profitto()

elettronica = Elettronica()
elettronica.calcola_profitto()
elettronica.mostra_garanzia()

abbigliamento = Abbigliamento()
abbigliamento.calcola_profitto()
abbigliamento.mostra_materiale()

fabbrica = Fabbrica()
fabbrica.aggiungi_prodotto()
fabbrica.mostra_inventario()
fabbrica.vendi_prodotto()
fabbrica.mostra_inventario()