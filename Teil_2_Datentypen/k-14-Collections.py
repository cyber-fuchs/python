# Kapitel 14 - Collections
import collections

gruppe_a =  {
        "Brasilien" : 7,
        "Mexiko"    : 7,
        "Kroatien"  : 5,
        "Kamerung"  : 0
}
gruppe_g =  {
        "Deutschland"   : 7,
        "USA"           : 4,
        "Portugal"      : 4,
        "Gahna"         : 1
}

gruppen = collections.ChainMap(gruppe_a, gruppe_g)
print("Brasilien mit",gruppen["Brasilien"], "Punkten gegen Deutschland mit", gruppen["Deutschland"],"Punkten" )

# Zählen von Häufigkeiten
t = "Dies ist ein Text"
d = {}
for c in t:
        if c in d:
                d[c] += 1
        else:
                d[c] = 1
print(d)

# Vereinfacht
t = "Dies ist ein Text"
d = collections.Counter()
for c in t:
        d[c] += 1
print(d)

# noch einfacher
print(collections.Counter("Dies ist ein Text"))

# d.elements() / Liste aller Elemente
# d.most_common([n]) / die häufigsten Elemente

# Wörter nach Länge sortieren

t = "if for else while elif with not and or try except"
d = {}
for wort in t.split():
        if len(wort) in d:
                d[len(wort)].append(wort)
        else:
                d[len(wort)] = [wort]
print(d)

# einfacher
t = "if for else while elif with not and or try except"
d = collections.defaultdict(list)
for wort in t.split():
        d[len(wort)].append(wort)
print(d)

# von 0 nach 9999
l = []
for x in range(10000):
        l.append(x)
print(x)

# von 9999 nach 0
l = []
for x in range(9999, -1,-1):
        l.insert(0,x)
print(x)

d = collections.deque([1,2,3,4])
d.appendleft(0)
d.append(5)
d.extendleft([-2,-1])
print(d)
d.rotate(4)
print(d)

import sys
print(sys.version_info)
print(sys.version_info.major)

Buch = collections.namedtuple("Buch", ["titel","autor","seitenanzahl","ISBN"])
py = Buch("The Art of Computer Programming", "Donald E. Knuth",3168, "978-0321751041")
print(py.autor)
print(py._fields)