"""Trasformate il programma che abbiamo creato in
precedenza per la gestione dei voti degli alunni in un
programma per la gestione di una classe che utilizza un
file come database:
All’avvio il programma chiede se si vuole leggere l’elenco
degli alunni e i loro voti e medie, se si vuole aggiungere un
alunno o un voto, se si vuole eliminare un alunno o un
voto."""

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

testo = """andrea:10,8,7,9
luca:6,9,10,7"""
nome_file = "es3.txt"
file = open(nome_file,"w")
file.write(testo)
