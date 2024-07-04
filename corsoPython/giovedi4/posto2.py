class Posto:
    def __init__(self, numero, fila, occupato=False):
        self._numero = numero
        self._fila = fila
        self._occupato = occupato
        self.lista_servizi = []

    def prenota(self):
        if self._occupato:
            print("Il posto non è prenotabile perchè già occupato")
        else:
            self._occupato = True
            print("Hai prenotato un posto")

    def libera(self):
        if not self._occupato:
            scelta = input("Il posto è libero, vuoi prenotarlo? (si/no): ")
            if scelta.lower() == 'no':
                print("Va bene, posto vuoto")
            elif scelta.lower() == 'si':
                self._occupato = True
                print("Hai prenotato il posto")
            else:
                print("Scelta non valida")
        else:
            self._occupato = False
            print("Hai liberato il posto")

    def get_numero(self):
        return self._numero

    def get_fila(self):
        return self._fila

    def get_stato(self):
        return self._occupato

class PostoVip(Posto):
    def __init__(self, numero, fila, occupato=False):
        super().__init__(numero, fila, occupato)
        self.extra = []

    def prenota(self):
        super().prenota()
        if self._occupato:
            scelta2 = input("Vuoi inserire servizi extra?(si/no): ")
            if scelta2.lower() == 'no':
                print("Va bene")
            elif scelta2.lower() == 'si':
                inserisci_extra = input("Quale extra vuoi aggiungere?: ")
                if inserisci_extra not in self.extra:
                    self.extra.append(inserisci_extra)
                    print(f"Servizio {inserisci_extra} aggiunto ai tuoi extra.")
                else:
                    print("Questo servizio è già presente nei tuoi extra")
            print(f"Servizi extra: {self.extra}")

    def posto_standard(self):
        def __init__(self, numero, fila, occupato=False):
            super().__init__(numero, fila, occupato)
            costo_aggiuntivo = False

            scelta_costi = input("Vuoi prenotare online?(si/no)")
            if scelta_costi == 'no':
                print("Nessun costo aggiuntivo")
            elif scelta_costi == 'si':
                costo_aggiuntivo == True
                print("Costi aggiuntivi addebitati")
            else:
                print("Errore")
        
    def libera(self):
        super().libera()
        if not self._occupato:
            self.extra = []  # Pulisce i servizi extra quando il posto viene liberato
            print("Servizi extra sono stati rimossi")


#l'interazione si fa dal mennu,non dalle classi
# Esempio di utilizzo
posto = Posto(1, 'A')
posto.prenota()
posto.libera()

posto_vip = PostoVip(2, 'B')
posto_vip.prenota()
posto_vip.libera()
posto_vip.posto_standard()