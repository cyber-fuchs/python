# Kapitel 17 - Funktionen
print("Einführung".center(40,"-"))

ergebnis = range(0,10,2)
for i in ergebnis:
    print(i)

liste = list(ergebnis)
print(liste)
print(liste[3])
print("Schreiben einer Funktion".center(40,"-"))
print("Fakultät".center(40,"-"))

def fak(zahl):
    if zahl < 0:
        return None
    ergebnis = 1
    for i in range(2,zahl+1):
        ergebnis *= i;
    return(ergebnis)

while True:
    eingabe = int(input("Geben Sie eine Zahl ein:"))
    ergebnis=fak(eingabe)
    if ergebnis is None:
        print("Fehler bei der Berechnung")
    elif eingabe == 0:
        break
    else:
        print(ergebnis)


print("Fakultät mit negativen Zahlen".center(40,"-"))
def betrag(zahl):
    if zahl < 0:
        return -zahl
    else:
        return zahl

def fak(zahl):
    ergebnis = 1
    for i in range(2,zahl+1):
        ergebnis *= i
    return ergebnis

while True:
    eingabe = int(input("Geben Sie eine Zahl ein:"))
    print(fak(betrag(eingabe)))
