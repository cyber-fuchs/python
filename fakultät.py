while True:
    zahl=int(input("Bitte geben Sie eine Zahl ein: "))
    if zahl < 0:
        print("bitte geben Sie eine positive Zahl ein.")
        continue
    ergebnis=1
    while zahl>0:
        ergebnis = ergebnis * zahl
        zahl =zahl-1
    print("Ergebnis: ", ergebnis)