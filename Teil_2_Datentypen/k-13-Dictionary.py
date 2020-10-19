# Kapitel 13 - Dictonary

woerterbuch = {
                "Germany" : "Deutschland",
                "Spain"   : "Spanien",
                "France"  : "Frankreich"
              }

for key in woerterbuch:
    print(key, woerterbuch[key])

woerterbuch["Greece"] = "Griechenland"
print(woerterbuch)

print("Thailand" not in woerterbuch)
dict2 = {
        "Vogel"    : "Adler",
        "Wildtier" : "fuchs",
        "Fisch"    : "Hai"
     }
print(dict2)
#dict2 |= {"Katze" : "Perser"}  #ab python3.9
#dict2 |= woerterbuch           #ab python3.9
#print(dict2)


# Methoden
# woerterbuch.clear() #löscht den Inhalt des dicts
# woerterbuch.copy() # Erzeugt eine Kopie
print(woerterbuch.get("Grönland",["Kann man das kaufen?"]))
print(woerterbuch.setdefault("Grönland","Kann man das kaufen?"))
print(woerterbuch.items())
print(woerterbuch.keys())
print(woerterbuch.update(dict2))
woerterbuch.pop("Grönland")
print(woerterbuch.values())

daten = ["k1","k2","k3"]
d = dict.fromkeys(daten,["Wert"])
dict.fromkeys([1,2,3],"python")
print(d)

