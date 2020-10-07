# Sequenzielle Datentypen
# list, tuple, str, bytes, bytearrayy
print("---Sequenzielle Datentypen---")

lst = ["eins",2,3.0,"vier",5,"sechs","sieben"]
print(lst)
print("Ist eine 3.0 in der Liste?:",3.0 in lst)
print("Ist eine 10 in der Liste?:",10 in lst)

s="Dies ist unser Teststring"
print(s)
print("Ist ein 'u' vorhanden?:", 'u' in s)

if 'j' in s:
    print("Juhuuu, ein j ist auch drin!")
else:
    print("Ich mag diesen String nicht.")

print("Ist ein 'ist' vorhanden?:", 'ist' in s)

print('"n" not in "Python ist toll":', "n" not in "Python ist toll")
print('not "n" in "Python ist toll":', not "n" in "Python ist toll")

# Verkettung von Sequenzen (+ und +=)
print("---Verkettung von Sequenzen (+ und +=)---")

vorname = "fuchs"
nachname = "bau"
name = vorname +" "+nachname
print (name)

s="Musik"
t="lautsprecher"
s+=t
print(s)

s =[1,2]
t=[3,4]
tmp = s
s += t
print(s)
print(tmp)

# Wiederholung von Sequenzen
print("---Wiederholung von Sequenzen---")
print(3*"abc")
weihnachtsmann = "ho"
weihnachtsmann *= 3
print(weihnachtsmann)
print(s)
print(s*3)

# Zugriff auf bestimmte Elemente einer Sequenz
print("--- Zugriff auf bestimmte Elemente einer Sequenz ---")

alphabet ="abcdefghijklmnopqrstuvwxyz"
print(alphabet)
print(alphabet[9])

s="schrottWichtigschrott"
print(s)
print(s[7:14])

l = ["ich","bin","eine","Liste","von","Strings"]
print(l)
print(l[2:5])
print(l[1:-1])

print(alphabet)
print(alphabet[:5])
print(alphabet[5:])

ziffern="0123456789"
print(ziffern)
print(ziffern[1::2])

name = "ytnoM Python"
print(name)
print(name[4::-1])
print(name[::-1])


# Länge einer Sequenz
print("---Länge einer Sequenz---")
string = "Wie lange bin ich wohl?"
print(string)
print(len(string))

# Kleinste und das größte Element
print("---Kleinste und das größte Element---")
s=[5,1,10,-9.5,12,-5]
print(s)
print(max(s))
print(min(s))

# Position eines Elementes in der Sequenz
print("---Position eines Elementes in der Sequenz---")
ziffern = [1,2,3,4,5,6,7,8,9]
print(ziffern)
print(ziffern.index(3))
print(name)
print(name.index("n"))

# Anzahl der Vorkommen eines Elements der Sequenz - s.count(x)
print("---Anzahl der Vorkommen eines Elements der Sequenz - s.count(x)---")
s=[1,2,2,3,2]
print(s)
print("So oft ist die 2 enthalten:",s.count(2),"mal.")
