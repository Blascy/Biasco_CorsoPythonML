#Scrivete un programma che riceve in input una stringa lunga e verifica se ci sono duplicati, 
#quanti sono, quali sono e quanto sono lunghi i duplicati. Esempio: ‘La casa è grande,
#una cucina una camera e un giardino. La cucina è piccola e la camera è spaziosa. Il giardino è verde e fiorito.’
#outpout "La" appare 2 volte, lunghezza 2

def duplicati(s):
    # Crea un insieme vuoto per tenere traccia dei caratteri visti
    visto = set()

    # Itera su ciascun carattere nella stringa
    for char in s:
        # Se il carattere è già nell'insieme, ci sono duplicati
        if char in visto:
            return True
        # Aggiunge il carattere all'insieme
        visto.add(char)
    
    # Se non abbiamo trovato duplicati, ritorna False
    return False

# Chiede all'utente di inserire una stringa
frase = input("Scrivi una frase: ")

# Verifica duplicati
if duplicati(frase):
    print("La stringa contiene duplicati.")
else:
    print("La stringa non contiene duplicati.")
