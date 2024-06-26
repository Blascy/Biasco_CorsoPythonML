def is_palindrome(s):
    # Rimuove gli spazi e converte la stringa in minuscolo
    s = ''.join(s.split()).lower()  #split rimuove spazi, lower rende minuscolo
    # Confronta la stringa con la sua versione invertita
    return s == s[::-1] #è come se fosse 0:: cioè parte dalla prima parola
    
# Chiede all'utente di inserire una parola o frase
parola = input("Inserisci una parola o frase: ")

# Verifica se la parola o frase inserita è una palindroma
if is_palindrome(parola):
    print(f"'{parola}' è una palindroma.")
else:
    print(f"'{parola}' non è una palindroma.")