"""Create un gestionale per la vostra squadra di calcio, siete gli allenatori quindi potete aggiungere massimo 25 calciatori:
- 3 portieri;
- 8 difensori;
- 8 centrocampisti;
- 6 attaccanti;
per ogni calciatore nome e ruolo.
Nel menù potete aggiungerli, eliminarli o visualizzarli, tutto verrà salvato in un database .txt"""

def leggi_db_calciatori():
    with open('fantacalcio.csv','r') as file:
        db_calciatori = file.read()
        return db_calciatori

def aggiungi_calciatori():
    nome = input("Inserisci nome del calciatore: ")
    ruolo = input('Inserisci ruolo del calciatore: ')
    nome_ruolo = nome + ',' + ruolo
    with open('fantacalcio.csv','a') as file:
        file.write(nome_ruolo)



def elimina_calciatori():
    contenuto = leggi_db_calciatori()
    print(contenuto)
    nome = input("Inserisci nome del calciatore: ")
    ruolo = input('Inserisci ruolo del calciatore: ')
    nome_ruolo = nome + ',' + ruolo
    contenuto = contenuto.split("\n") #a che serve \n? andare a capo?
    if nome_ruolo in contenuto:
        contenuto.remove(nome_ruolo)
    contenuto = "\n".join(contenuto)
    with open('fantacalcio.csv','w') as file:
        file.write(contenuto)

db = leggi_db_calciatori()

def conto_ruoli():
    return db
    if ruolo == 'portiere':

