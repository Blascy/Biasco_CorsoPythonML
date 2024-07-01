"""
Dobbiamo creare un programma per la gestione di una biblioteca,
all'avvio del programma ci viene chiesto se siamo amministratori o utenti,
se siamo amministratori possiamo vedere i libri, aggiungere un libro
eliminare un libro.
il libro ha le seguenti caratteristiche:
- titolo
- autore
- anno
- stato prestito
"""
import pickle

def conversione_salvataggio_libro(dato):
    if len(dato) >1:
        righe = []
        for riga in dato:
            righe.append(",".join(riga))
        righe = "\n".join(righe)
    else:
        righe = ",".join(dato)
    
    return righe



def leggi_db_libri():
    with open("db_libri.csv", "r") as file:
        db_libri = file.read()
    return db_libri

def leggi_db_utenti():
    with open("db_untenti.bin", "rb") as file:
        db_utenti = pickle.loads(file.read())
    return db_utenti


def verifica_db():
    try:
        db_utenti = leggi_db_utenti()
    except:
        user = input("Inserisci un nome utente: ")
        psw = input("Inserisci un nome utente: ")
        dizionario = {"amministratori":{user:psw},"utenti":{}}
        scrivi_utenti(dizionario)
        db_utenti = leggi_db_utenti()   
    libr_vuoti = True
    try:
        db_libri = leggi_db_libri()
    except:
        scrivi_libri("")
        db_libri = leggi_db_libri()
    
    if len(db_libri) >0:
        libr_vuoti = False

    return db_utenti , db_libri, libr_vuoti

def scrivi_libri(dato, metodo):
    with open("db_libri.csv", metodo) as file:
            file.write(dato)

def scrivi_utenti(dato):
    dato_b = pickle.dumps(dato)
    with open("db_untenti.bin", "wb") as file:
            file.write(dato_b)

def aggiungi_utente_a():
    ruolo = input("1 per ruolo amministratore\n2 per ruolo 'utente': ")
    ruolo_ok = True
    if ruolo == "1":
        chiave = "amministratori"
    elif ruolo == "2":
        chiave = "utenti"
    else:
        print("Ruolo non valido!")
        ruolo_ok = False
    
    if ruolo_ok:
        user = input("Inserisci user: ")
        if user in db_utenti[chiave]:
            print("Utente già presente!")
        else:
            psw = input("Inserisci password: ")
            db_utenti[chiave][user]= psw
            scrivi_utenti(db_utenti)
            print("Utente aggiunto")


def inserisci_libro():
    titolo = input("Inserisci il titolo del libro: ")
    autore = input("Inserisci il autore del libro: ")
    anno = input("Inserisci anno del libro: ")
    stato = "libero"
    nuovo_libro =titolo+","+autore+","+anno+","+stato
    if libr_vuoti:
        scrivi_libri(nuovo_libro, "a")
        
    else:
        scrivi_libri("\n"+nuovo_libro,"a")
... (180 righe a disposizione)