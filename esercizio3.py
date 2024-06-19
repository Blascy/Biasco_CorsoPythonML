requisiti = {
    "eta" : 18
}

eta_utente = (int(input("Quanti anni hai? ")))
if eta_utente < requisiti["eta"]:
    print("Mi dispiace, non puoi vedere questo film")
else:
    print("Puoi vedere questo film!")

