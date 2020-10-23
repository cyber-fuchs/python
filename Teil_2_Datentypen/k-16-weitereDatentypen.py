# Kapitel 16 - Weitere Datentypen
import enum
line = "-----------------------------"

class Wochentag(enum.Enum):
    Montag = 1      # Montag = enum.auto() ist ab python3.6 möglich
    Dienstag = 2
    Mittwoch = 3
    Donnerstag = 4
    Freitag = 5
    Samstag = 6
    Sonntag = 7

print(line)
print(Wochentag.Samstag)
print(Wochentag(3))
print(Wochentag["Montag"])

print(line)
for tag in Wochentag:
    print(tag)
print(line)

class Ampel(enum.Flag):
    Rot = enum.auto()
    Gelb = enum.auto()
    Gruen = enum.auto()

combo_zustand = Ampel.Rot |Ampel.Gelb
print(combo_zustand & Ampel.Rot)
print(line)
# Datenklassen / Liste / Dictonarys / Benannte Tupel

adresse = ("Domkloster", 4, 50667, "Köln")
print(adresse[2])
print(line)

adresse = {
        "straße" : "Domkloster",
        "hausnummer" : 4,
        "plz" : 50667,
        "stadt" : "Köln"
}
print(adresse["straße"])
print(line)

import collections
addr = collections.namedtuple(
    "addr",
    ("straße","hausnummer","plz","stadt")
)
adresse = addr("Domkloster",4,50667,"Köln")
print(adresse)
print(adresse.hausnummer)
print(line)

import dataclasses
@dataclasses.dataclass()
class Adresse:
    strasse: str
    hausnummer: int
    plz: int
    stadt: str = ""
    def __post_init__(self):
        if not self.stadt and self.plz == 50667:
            self.stadt = "Köln"

adresse = Adresse("Domkloster",4,50667)
print(adresse)
print(line)
