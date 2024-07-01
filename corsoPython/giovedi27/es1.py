"""Crea un programma che gestisca una lista di contatti. Ogni contatto avrà un nome, un cognome, 
e un numero di telefono. 
Il programma dovrà permettere di aggiungere nuovi contatti e visualizzare tutti i contatti esistenti, 
salvandoli in un file CSV."""
import csv

file_path = "giovedi27\contatti.csv"

with open(file_path,"r") as file:
    reader = csv.reader(file)
print(file)