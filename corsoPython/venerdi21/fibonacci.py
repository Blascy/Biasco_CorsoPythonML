def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

scelta = int(input("Sequenza di fibonacci con: "))

for i in range(0,scelta):
    print(fibonacci(i), end = " ")


