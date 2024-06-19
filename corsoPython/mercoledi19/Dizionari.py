studente = {
    "nome" : "Andrea",
    "eta" : 23,
    "sesso" : "Maschile"
}

#modifico i valori del dizionario
studente["eta"] = 22
studente["nome"] = "Michele"
print(studente)

#aggiungo una nuova chiave=citta con valore=roma
studente["citta"] = "Roma"
print(studente)

#metodi: keys(), values(),items(),get()
print(studente.keys()) #stampa nome eta sesso citta
print(studente.values())#stampa Michele,22,Maschile,Roma
print(studente.items())#stampa le coppe tra parentesi tipo (citta,Roma), (nome,Michele)
print(studente.get("eta")) #stampa la chiave dell'eta