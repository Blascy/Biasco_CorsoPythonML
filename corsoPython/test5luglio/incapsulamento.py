"""
L'incapsulamento è una tecnica di progettazione che implica il raggruppamento di entità correlate
all'interno di una "capsula" concettuale. Questo processo di impacchettamento crea una barriera tra
l'interno della capsula e il resto del sistema. L'incapsulamento viene spesso associato all'astrazione e
coinvolge la creazione di un'entità chiamata "pacchetto" che contiene i dati e i metodi correlati. L'obiettivo
dell'incapsulamento è proteggere i dati all'interno della capsula e fornire un'interfaccia controllata per
accedervi. Le tecniche di programmazione associate all'incapsulamento consentono di definire regole e
restrizioni sull'accesso e la manipolazione dei dati. In altre parole, l'incapsulamento definisce come i dati
devono essere gestiti e nascosti all'esterno della capsula. Le "pareti" della capsula possono essere di diversi
tipi. Possono essere trasparenti, consentendo la visualizzazione completa di ciò che è stato incapsulato.
Possono essere traslucide, permettendo una visione parziale del contenuto. Oppure possono essere
opache, nascondendo completamente il contenuto del pacchetto
Alcuni esempi dell'incapsulamento:
Attributi Privati (__attributo)
due underscore (__) al nome di un attributo, questo diventa privato, 
il che significa che non può essere accesso direttamente dall'esterno della classe. 
Per accedere o modificare un attributo privato, si usano i metodi getter e setter.

Attributi Protetti (_attributo)
un underscore (_) al nome di un attributo, questo viene considerato protetto. 
Si tratta più di una convenzione che di una funzionalità linguistica, 
indicando che l'attributo dovrebbe essere usato solo all'interno della classe e delle sue sottoclassi.

Metodi Getter e Setter
Sono metodi che permettono di ottenere (get) e modificare (set) gli attributi privati di una classe. 
Questi metodi forniscono un controllo maggiore sull'accesso e la modifica dei dati.

Scope delle Variabili
Local
Le variabili locali sono definite all'interno di una funzione e possono essere utilizzate solo all'interno di 
quella funzione. Non sono accessibili al di fuori di essa.

Global
Le variabili globali sono definite al di fuori di qualsiasi funzione e sono accessibili da qualsiasi punto del programma. 
Per modificare una variabile globale all'interno di una funzione, si utilizza la parola chiave global.

Nonlocal
Le variabili nonlocal sono utilizzate nelle funzioni annidate. 
La parola chiave nonlocal permette di accedere a variabili definite in uno scope esterno ma non globale, 
come ad esempio nelle funzioni interne.
"""
class ContoBancario:
    def __init__(self, titolare, saldo_iniziale):
        self.titolare = titolare
        self.__saldo = saldo_iniziale

    def get_saldo(self):
        return self.__saldo

    def deposita(self, quantità):
        self.__saldo += quantità
        print(f"Depositati {quantità}€. Saldo aggiornato: {self.__saldo}€.")

    def preleva(self, quantità):
        self.__saldo -= quantità
        print(f"Prelevati {quantità}€. Saldo residuo: {self.__saldo}€.")

conto = ContoBancario("Mario Rossi", 1000)
print(f"Saldo iniziale: {conto.get_saldo()}€")
conto.deposita(500)
conto.preleva(200)

# Tentativo di accesso diretto all'attributo privato (__saldo) - questo genererà un errore
print(conto.__saldo)
