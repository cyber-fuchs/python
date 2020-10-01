woerter={}
beenden=["quit","exit","q"]

fobj  = open("woerterbuch.txt","r")

for line in fobj:
    line = line.strip()     #entfernt alle Whitespace Zeichen
    zuordnung = line.split(';')
    woerter[zuordnung[0]] = zuordnung[1]
fobj.close


while True:
    wort = input("Geben Sie ein Wort ein: ")
    if wort in woerter:
        print("Das deutsche Wort lautet: ",woerter[wort])
    elif wort in beenden:
        break
    else:
        print("Das Wort ist unbekannt")


