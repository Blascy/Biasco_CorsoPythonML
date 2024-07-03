class ContoBancario:
    def __init__(self, titolare):
        # Li ho dichiarati come attributi protetti (_attributo)
        self._titolare = titolare
        self._saldo = 0.0

    def mostra_titolare(self):
        return self._titolare

    def deposita(self, importo):
        if importo > 0:
            self._saldo += importo
            print(f"L'importo di {importo} euro è stato aggiunto")
        else:
            print("L'importo deve essere maggiore di zero")

    def preleva(self, importo):
        if importo <= self._saldo and importo > 0:
            self._saldo -= importo
            print(f"Prelievo di {importo} euro eseguito correttamente")
        else:
            print("Importo non valido o saldo insufficiente")

    def mostra_saldo(self):
        print(f"Il saldo corrente è di {self._saldo} euro")


# Esempio di utilizzo
titolare = input("Inserisci il nome del titolare del conto bancario: ")
contoAndrea = ContoBancario(titolare)

print(f"Titolare del conto: {contoAndrea.mostra_titolare()}")

importo = float(input("Inserisci un importo da depositare: "))
contoAndrea.deposita(importo)
importo_prelievo = float(input("Inserisci un importo da prelevare: "))
contoAndrea.preleva(importo_prelievo)
contoAndrea.mostra_saldo()
