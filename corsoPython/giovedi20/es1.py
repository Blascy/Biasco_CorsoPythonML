#scelta = int(input("Inserisci un numero: "))

#while True:
    # for i in range(scelta,0,-1):
#print(i)

    #scelta2 = (input("\nVuoi ripetere? (si/no)"))
    #if scelta2 == si:
      #  scelta = int(input("Inserisci un numero: "))
      #  else
       # print("Arrivederci")

controllo = True
while controllo:
    scelta = int(input("Inserisci un numero: "))

    for i in range(scelta, 0, -1):
        print(i)

    scelta2 = input("\nVuoi ripetere? (si/no): ")
    if scelta2.lower() == "si":
        continue  # Riprende il ciclo while per chiedere un nuovo numero
    else:
        print("Arrivederci")
        controllo = False
