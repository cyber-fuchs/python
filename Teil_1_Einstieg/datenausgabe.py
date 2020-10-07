woerter={'Spain': 'Spanien', 'Germany': 'Deutschland', 'Sweden': 'Schweden', 'France': 'Frankreich', 'Italy': 'Italien'}

fobj = open("ausgabe.txt","w")
for engl in woerter:
    fobj.write("{} {}\n".format(engl, woerter[engl]))
fobj.close


""" open Modus:
"r" = lesen
"w" = schreiben
"a" = schreiben / erzeugt keine neue Datei
"x" = wie "a" nur mit Fehlermehlung
"rb/wb/ab.." = Datei wird im Binärmodus geöffnet
"""
