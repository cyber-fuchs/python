woerter={}

with open("woerterbuch.txt", "r") as fobj:
    for line in fobj:
        line = line.strip()
        zuordnung = line.split(";")
        woerter[zuordnung[0]] = zuordnung[1]
    pass
print(woerter)
