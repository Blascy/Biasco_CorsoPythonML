def area_triangolo(base,altezza):
    return (base_t*altezza_t) /2

def area_rettangolo(base,altezza):
    return (base_r*altezza_r)

#manca il quadrato


#Input della base e altezza del triangolo
base_t = float(input("Inserisci la base del triangolo: "))
altezza_t = float(input("Inserisci l'altezza del triangolo: "))

#Input della base e altezza del rettangolo
base_r = float(input("Inserisci la base del rettangolo: "))
altezza_r = float(input("Inserisci l'altezza del rettangolo: "))

#calcolo e stampa area
area_t = area_triangolo(base_t,altezza_t)
area_r = area_rettangolo(base_r,altezza_r)
print("Area del triangolo: ",area_t)
print("Area del rettangolo: ",area_r)


