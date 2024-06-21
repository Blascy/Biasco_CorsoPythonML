vocali = "aeiouAEIOU"
inserisci= input("Inserisci una stringa: ")

#contatore vocali
contatore = 0

#itera carattere nella stringa per trovare le vocali e tenerne traccia tramite variabile contatore
for c in inserisci:
    if c in vocali:
        contatore += 1

# Stampare il risultato
print(f"Nella stringa '{inserisci}' ci sono {contatore} vocali.")