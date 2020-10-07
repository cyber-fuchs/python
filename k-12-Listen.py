# Kapitel 12 - Datentypen (Listen)

# Verändern eines Wertes innerhalb der Liste
print("---# Verändern eines Wertes innerhalb der Liste---")
print("---Kapitel 12 - Datentypen (Listen)---")

s = [1,2,3,4,5,6,7]
print(s)
s[3] = 1337
print("s[3]=1337")
print(s)

# Ersetzen von Teillisten und Einfügen neuer Elemente
print("---Ersetzen von Teillisten und Einfügen neuer Elemente---")
einkaufen = ["Brot","Eier","Milch","Fisch","Mehl"]
print(einkaufen)
einkaufen[1:3]=["Bier","Erdnüsse"]
print('einkaufen[1:3]=["Bier","Erdnüsse"]')
print(einkaufen)

s =[0,1,2,3,4,5,6,7,8,9,10,11]
print(s)
s[2:9:3]=["A","B","C"]
print(s)

# Elemente und Teillisten löschen
print("---Elemente und Teillisten löschen---")
s=[26,7,1987]
print(s)
del s[0]
print(s)


s=[9,8,7,6,5,4,3,2,1]
print(s)
del s[3:6]
print(s)

s=["a","b","c","d","e","f","g","h","i","j"]
print(s)
del s[::2]
print(s)

# Methoden von Listen 
print("---Methoden von Listen---")

# s.append
s = ["Nach mir soll noch ein String stehen."]
s.append("Hier ist er")
print(s)

#s.extend
s=[1,2,3]
print(s)
s.extend([4,5,6])
print(s)

# s.insert
del s[3]
print(s)
s.insert(3,4)
print(s)

#s.pop
s = ["H","a","l","l","o"]
s.pop()
print(s)
s.pop(0)
print(s)

#s.remove
s = ["H","a","l","l","o"]
print(s)
s.remove("a")
print(s)

# s.reverse()
s = [1,2,3]
print(s)
s.reverse()
print(s)

#s.sort([key, reverse])
s = [4,2,7,9,1,2,6,3]
print(s)
s.sort()
print(s)
