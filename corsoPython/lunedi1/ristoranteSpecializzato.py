class Ristorante:

    def __init__(self):
        self.nome = input("Inserisci il nome del ristorante: ")
        self.tipo_cucina = input("Inserisci il tipo di cucina del ristorante: ")
        self.aperto = False
        self.menu = {}


    def descrivi_ristorante(self):
        print(f"Il ristorante si chiama {self.nome} e offre un tipo di cucina {self.tipo_cucina}")


    def stato_apertura(self):
        if self.aperto:
            print("Il ristorante è aperto")
        else:
            print("Il ristorante è chiuso")


    def apri_ristorante(self):
        if not self.aperto:
            self.aperto = True
            print("Ora il ristorante è aperto")


    def chiudi_ristorante(self):
        if self.aperto:
            self.aperto = False
            print("Ora il ristorante è chiuso")


    def aggiungi_al_menu(self):
        aggiunta_piatti = input("Aggiungi un piatto al menu: ")
        aggiunta_prezzi = int(input("Aggiungi prezzo del piatto: "))
        self.menu[aggiunta_piatti] = aggiunta_prezzi
        print(f"Piatto '{aggiunta_piatti}' aggiunto al menu con prezzo {aggiunta_prezzi}")


    def togli_dal_menu(self):
        if self.menu:
            nome_piatto = input("Inserisci il nome del piatto da eliminare: ")
            if nome_piatto in self.menu:
                del self.menu[nome_piatto]
                print(f"Piatto '{nome_piatto}' eliminato dal menu")
            else:
                print("Piatto non trovato nel menu")
        else:
            print("Il menu è vuoto, non ci sono piatti da eliminare")


    def stampa_menu(self):
        if self.menu:
            print("Menu:")
            for piatto, prezzo in self.menu.items():
                print(f"{piatto}: {prezzo} Euro")
        else:
            print("Il menu è vuoto.")


    def ordinazione_utente(self):
        if not self.menu:
            print("Il menu è vuoto. Non ci sono piatti da ordinare.")
            return


        print("Menu disponibile:")
        for piatto in self.menu:
            print(piatto)


        scelta_piatto = input("Quale piatto vuoi ordinare tra questi? ")
        if scelta_piatto in self.menu:
            conferma = input(f"Hai scelto '{scelta_piatto}'. Confermi l'ordinazione? (si/no) ")
            if conferma.lower() == 'si':
                print(f"Piatto '{scelta_piatto}' ordinato.")
            else:
                print("Ordinazione annullata.")
        else:
            print("Il piatto scelto non è disponibile nel menu.")


    def stampa_menu_principale(self):
        print("Menu principale:")
        print("1. Opzione 1: Vuoi conoscere il ristorante?")
        print("2. Opzione 2: Vuoi sapere se il ristorante è aperto o chiuso?")
        print("3. Opzione 3: Vuoi aggiungere un piatto al menu?")
        print("4. Opzione 4: Vuoi rimuovere un piatto dal menu?")
        print("5. Opzione 5: Vuoi vedere il menu?")
        print("6. Opzione 6: Vuoi ordinare un piatto?")
        print("7. Esci")
        

    def esegui_menu(self):
        while True:
            self.stampa_menu_principale()
            scelta = input("Scegli un'opzione (1-6): ")

            if scelta == '1':
                self.descrivi_ristorante()
            elif scelta == '2':
                self.stato_apertura()
            elif scelta == '3':
                self.aggiungi_al_menu()
            elif scelta == '4':
                self.togli_dal_menu()
            elif scelta == '5':
                self.stampa_menu()
            elif scelta == '6':
                self.ordinazione_utente()
            elif scelta == '7':
                print("Uscita dal programma.")
                break
            else:
                print("Scelta non valida. Scegli un'opzione valida (1-6).")


# Creo oggetto della classe Ristorante
ristoranteFoggia = Ristorante()
ristoranteFoggia.esegui_menu()
