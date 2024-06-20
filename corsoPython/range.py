#è una funzione che restituisce una sequenza di interi che possono essere calcolati in cicli for o altre situazioni
#in cui si puo iterare in un insieme di valori
#range essenzialmente serve a fare la conta, simile a for di java ma questa è una funzione
#sintassi
range([start],stop,[step])
#start è opzionale, se omesso di default è 0
#stop è obbligatorio
#step è opzionale

for i in range(5):
    print(i)

for x in range(1,10,5):
    print (x)