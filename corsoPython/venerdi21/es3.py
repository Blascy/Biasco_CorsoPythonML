#scrivi programma che utilizzi un ciclo for con range per stampare fino a un massimo N 
# dato dall'utente tramite uno steps dato dall'utente (es 2 passi per volta) #solo
while True:
    inserisci = int(input("Inserisci numero massimo: "))
    step = int(input("Inserisci step numerico: "))

    for n in range(0, inserisci, step):
        print(n)

    continua = input("Vuoi continuare? (sì/no): ").strip().lower()
    if continua != 'sì':
        print("Arrivederci")
        break


