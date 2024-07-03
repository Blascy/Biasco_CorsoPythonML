class Posto:
    def __init__(self, numero, fila, occupato=False):
        self._numero = numero
        self._fila = fila
        self._occupato = occupato

    def prenota(self):
        if self._occupato: #non avrebbe senso scrivere se self._occupato = false perche gia falso
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
        def __init__(self,numero, fila, occupato=False,servizi_extra):
            super().__init__(numero, fila, occupato=False)
            self.servizi_extra = servizi_extra

        def prenota(self,servizi_extra):
            print(f"Servizi extra: {servizi_extra}")

    

# Esempio di utilizzo
inserisci_numero = int(input("Inserisci il numero del posto: "))
inserisci_fila = input("Inserisci la fila in cui si trova il posto: ")

# Utilizzo degli oggetti Posto
posto1 = Posto(inserisci_numero, inserisci_fila)

posto1.prenota()
posto1.libera()
print(f"Numero del posto: {posto1.get_numero()}")
print(f"Fila del posto: {posto1.get_fila()}")
print(f"Stato del posto: {'Occupato' if posto1.get_stato() else 'Libero'}")
