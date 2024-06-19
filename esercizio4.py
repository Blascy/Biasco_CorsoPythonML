primo_numero = int(input("Inserisci un primo numero: "))
secondo_numero = int(input("Inserisci un secondo numero: "))
operazione = input("Inserisci l'operazione (+, -, *, /): ")

if primo_numero > 0 and secondo_numero > 0:
    if operazione == "+":
        risultato = primo_numero + secondo_numero
    elif operazione == "-":
        risultato = primo_numero - secondo_numero
    elif operazione == "*":
        risultato = primo_numero * secondo_numero
    elif operazione == "/":
        if secondo_numero == 0:
            print("Errore: divisione per zero.")
        else:
            risultato = primo_numero / secondo_numero
            print(f"Il risultato dell'operazione è: {risultato}")
    else:
        print("Operazione non valida. Inserisci +, -, *, o /.")
else:
    print("Entrambi i numeri devono essere maggiori di zero.")
