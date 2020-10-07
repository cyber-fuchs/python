while True:
    zahl=int(input("Bitte Zahl eingeben: "))
    if zahl<0:
        print("Bitte eine positive Zahl eingeben.")
        continue
    ergebnis = 1
    for i in range(2, zahl+1):
        ergebnis=ergebnis*i
    print("Ergebnis: ",ergebnis)