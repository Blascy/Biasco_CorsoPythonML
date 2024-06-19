#a differenza delle liste una volta creata una dupla non può essere modificata;
# le tuple raggruppano elementi correlati o singole entità
# liste vogliono parentesi quadra, tuple tonda

#errore
#punto = (3,4)
#punto[0] = 5

#si posson evitare le parentesi tonde "tuple packing" "tuple unpacking"
punto = 3,4,9,15
x,y,z,j= punto
print(punto.__reversed__(x,y,z,j))
print( x,y,z,j)
