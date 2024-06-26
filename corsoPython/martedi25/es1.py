#Scrivete un programma che prenda i nomi degli alunni di una
#classe e i loro voti, quando l’utente scrive media il programma
#andrà a stampare i nomi di tutti gli alunni e per ogni alunno la
#media dei voti.
#Esempio:
#Nome: Giovanni , Media: 7.5
#Nome: Alfredo , Media: 9
#Nome: Michela, Media 10

studenti = {}

while True:
    comando = input("Inserisci il nome dello studente o 'media' per conoscere le medie dei voti: ").strip()
    if comando.lower() == "media":
        if len(studenti) == 0:
            print("Nessun alunno presente")
        else:
            break
    else:
        studenti[comando] = []
        nvoti = int(input("Quanti voti vuoi inserire? "))
        for num in range(nvoti):
            voto = int(input("Inserisci il voto: "))
            studenti[comando].append(voto)

print("\nMedie dei voti degli studenti:")

for studente, voti in studenti.items():
    if len(voti) == 0:
        print(f"Nome: {studente}, Media: {0}")
    else:
        media = sum(voti) / len(voti)
        print(f"Nome: {studente}, Media: {media:.2f}")
