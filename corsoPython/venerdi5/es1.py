"""Create un gestionale bancario basato sulla programmazione a oggetti,
la prima parte dell'esercizio riguarda solamente aggiunta e eliminazione cliente con il suo conto bancario e modifica 
cliente"""

"""seconda parte esercizio il cliente può fare:
- un pagamento;
- un deposito;
- un ritiro."""
class Banca:

    dizionario = {}

    def init(self):
        pass

    def aggiungi_cliente(self):
        while True: 
            nome_utente = input("Scrivi il tuo nome: ")
            codice_utente = input("Scrivi il tuo codice: ")

            if codice_utente not in Banca.dizionario:
                Banca.dizionario[codice_utente] = nome_utente
                print(f"Cliente {nome_utente} aggiunto con successo.")
                print(Banca.dizionario)
            else:
                print("Codice presente. Esiste già un conto bancario con questo codice.")

            continua = input("Vuoi aggiungere un altro cliente? (si/no) ")
            if continua.lower() != "si":
                break

    def rimuovi_cliente(self):
        codice_utente = input("Inserisci il codice del cliente di cui vuoi eliminare il conto: ")

        if codice_utente in Banca.dizionario:
            del Banca.dizionario[codice_utente]
            print("Cliente rimosso!")
            print(Banca.dizionario)
        else:
            print("Non c'è nessun cliente da rimuovere con questo codice.")

    


banca = Banca()
banca.aggiungi_cliente()
banca.rimuovi_cliente()
