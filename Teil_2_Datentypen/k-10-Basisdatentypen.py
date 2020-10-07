# Datentypen
# Nummerische Datentypen: int, float, bool, complex
# Sequenzielle Datentypen: list, tuple, str, bytes, bytearray
# Zuordnung und Mengen: dict, set, frozenset

x = "Hallo"
print(type(x))

#das Nichts
ref = None
print(ref)
#Prüfung ob eine Referenz auf None verweist
if ref is None:
    print("ref ist None")

a = 2
b = 5
c = 7
d = 10
e = 15

# a < b < c == a < b and d > c
print(a<b<=c != d > e)
print(a<b and b<=c != d and d>e)