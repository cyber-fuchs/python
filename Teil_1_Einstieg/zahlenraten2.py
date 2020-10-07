geheimnis=1337
versuch=-1
zaehler=0

while versuch != geheimnis:     #and versuch !=0 //auch ne Möglichkeit
    versuch=int(input("Rate Sie: "))

    if versuch == 0:
        print("Spiel wird beendet")
        break

    if versuch < geheimnis:
        print("zu klein")

    if versuch > geheimnis:
        print("zu groß")
    
    zaehler+=1

else: print("Sie haben es in ", zaehler," Versuchen erraten!")



