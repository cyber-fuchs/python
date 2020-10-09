# Kapitel 12 - Strings
print("---Kapitel 12 Strings---")
print("---Steuerzeichen---")
a="Erste Zeile\nZeite Zeile"
print(a)

# \a - Bell / \b Backspace / \t - Tabulator / \n - new Line ...

print("---STring-Methoden---")

# s.split
print("\nMethode s.split([sep,maxsplit]) und s.rsplit")
s = "1-2-3-4-5-6-7-8-9-0"
print(s)
print(s.split("-"))
print(s.split("-",5))
print(s.rsplit("-",5))

s = "1---3-4-5"
print(s)
print(s.split("-"))

s = "a b c d e f g h i j k l m n o p"
slist = s.split()
print(slist)

s = "Irgendein Satz \t\t mit Whitespaces"
print(s)
print(s.split())

print("\nMethode s.splitlines")
s = "Unix\nWindows\nMac\nLetzte Zeile"
print(s)
print(s.splitlines())

print("\nMethode s.partition und s.rpartition")
s = "www.rheinwerk-verlag.de"
print(s)
print(s.partition("."))
print((s.rpartition(".")))

print("\nMethode s.find und s.rfind")
s = "Mal sehen wie oft das \"e\" in diesem Satz vorkommt?"
print(s)
print("An Stelle",s.find("e"),"das erste mal")
print("An Stelle",s.rfind("e"),"das letzte mal")

print("\nMethode s.index und s.rindex")
s = "Dieser String wird gleich durchsucht"
print(s,"\n",s.index("wird"))

s = "Fischers Fritz fischt frische Fische"
print(s,s.count("sch"))

print("\nErsetzen von Teil-Strings")
s = "Python ist nicht toll"
s = s.replace("nicht","richtig")
print(s)

s = "Bitte nur die ersten vier 'E' ersetzen"
print(s.replace("e","E",4))

s = "ERST GANZ GROSS UND DANN GANZ KLEIN!"
print(s.lower()) #s.upper ist der umgekehrte Fall

s = "wENN MAN DIE cAPS-lOCK tASTE GEDRÜCKT HATTE..."
print(s.swapcase())

s = "alles klein... noch :)"
print(s.capitalize())

s = "nOcH bIn ICH wEnIGER als TITEL GEeiGNET"
print(s.title())

s = ("\tHier kann Quellcode stehen\n" +
    "\t\tHier eine Ebene drunter")
print(s)
print(s.expandtabs(2))

print("\nString Methoden zum Entfernen bestimmter Zeichen")
s = "    \t\n  Umgeben von Whitespaces   \n\t"
print(s.strip())
#print(s.lstrip())
#print(s.rstrip())

ziffern ="0123456789"
s = "234823Versteckt zwischen Zahlen21312312312452309032"
print(s.strip(ziffern))

print("\nAusrichtung von Strings")
s = "Richte mich aus"
print(s.center(50))
print(s.ljust(50))
print(s.rjust(50, "-"))
print("13.37".zfill(20))

print("\nString Test")
s = "123abc"
s.isdigit()
s.isalpha()
s.isalnum()

s = "www.rheinwerk-verlag.de"
s.startswith("www")
s.endswith("de")
s.startswith("rheinwerk",4)

print("\nVerkettung")
s = "Fix Foxy Lupo Dr.Knox"
kontaktliste = s.split()
print(kontaktliste)
print(", ".join(kontaktliste))

satz = "Stoiber-Satz"
print("...ehm...".join(satz))

print(kontaktliste)
print(" ".join(kontaktliste))
