geheimnis=1337
versuch=-1
zaehler=0

while versuch != geheimnis:
    versuch=int(input("Rate Sie: "))

    if versuch < geheimnis:
        print("zu klein")

    if versuch > geheimnis:
        print("zu groß")

    zaehler+=1

print("Sie haben es in ", zaehler," Versuchen erraten!")


