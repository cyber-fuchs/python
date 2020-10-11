print("Formatierung von Strings".center(50))
print("Es ist {}:{} Uhr - Feierabend!".format(13,37))
print("Es ist {Stunde}:{Minute} Uhr - Feierabend!".format(Stunde=13,Minute=37))
stunde = 13
minute = 37
print(f"Es ist {stunde}:{minute} Uhr!")

# Formatierte Ausgabe
print("Beitrag: {:.2f}".format(13.378986))

# Minimale Breite festlegen
f = "{:15}| {:15}"
print(f.format("Vorname", "Nachname"))
print(f.format("fuchs", "bau"))
print(f.format("Dino", "Saurier"))
print(f.format("Ich bin länger als 15 Zeichen", "Ja"))

# Linksbündig: <    Rechtsbündig: >     Mitte: ^    Spez: =
print("Endpreis: {sum:>5} Euro".format(sum=443))
print("Endpreis: {sum:^5} Euro".format(sum=443))
print("Endpreis: {sum:=5} Euro".format(sum=-443))

# Füllzeichen
print("{text:-^25}".format(text="Hallo Welt"))

# Vorzeichen
x = -135
print(f"Kosten: {x:+10}")
print(f"Kosten: {x:=+10}")

# in Bytes
# b = binär; c = unicode; d = dezimal; o = oktal; x oder X = hexadezimal; n = dezimal mit Tausenderpunkten
# mit "#" werden nicht dezimalSysteme gekennzeichnet (0x = hexa 0o = okal)
print("In Bits: {zahl:#b}".format(zahl=109))
print("In Unicode: {zahl:c}".format(zahl=11))
print("In dezimal: {zahl:#d}".format(zahl=1337))
print("In Octal: {zahl:#o}".format(zahl=1337))
print("In Hex: {zahl:#x}".format(zahl=1237))
print("In Dezi: {zahl:n}".format(zahl=10342.337))

# Formatierung von Gleitkommazahlen
zahl = 123.456
print(f"{zahl:e}")
print(f"{zahl:f}")
print(f"{zahl:n}")
print(f"{zahl:%}")
print(f"{zahl:.2f}")


