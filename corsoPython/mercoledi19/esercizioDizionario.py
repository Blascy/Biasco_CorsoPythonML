#creare 3 input da riempire con booleano,intero e stringa. Li inserisco in una lista e inserisco la lista
# come valore di un dizionario con chiave 'tipodidato'

inserisco_booleano = bool(input("Inserisci un booleano: "))
inserisco_intero = int(input("Inserisci un valore per il dizionario: "))
inserisco_stringa = input("inserisci una stringa: ")

lista = [inserisco_booleano,inserisco_intero,inserisco_stringa]

dizionario = {
    "tipodidato" : lista
}

print(dizionario)