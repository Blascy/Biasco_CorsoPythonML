n1 = int(input("Inserisci il primo numero: "))
n2 = int(input("Inserisci il secondo numero: "))

operazione = input("Inserisci operazione matematica (+; /; **; *; -;): ")

if operazione == "+":
    print(n1 + n2)
elif operazione == "/":
    print(n1/n2)
elif operazione == "**":
    print(n1**n2)
elif operazione == "*":
    print(n1*n2)
elif operazione == "-":
    print(n1-n2)


