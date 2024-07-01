lista = [ "Tommaso", "Alfredo", "Giovanni", "Tobia"]

def funz(elem):
    if "T" in elem:
        return True
    else:
            return False

list2 = list(filter(funz,lista)) 

print(list2) #tommaso e tobia