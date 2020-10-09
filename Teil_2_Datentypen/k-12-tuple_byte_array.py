# Kapitel 12 - Tuple uns Byte Array

print("---Unveränderliche Listen---")
a = (1,2,3,4,5)
print(a[3])
print(type(a))


# Packing und Unpacking
print("---Packing und Unpacking---")
datum = 26,7,1987
print(datum)
(tag, monat, jahr) = datum
print(jahr, monat, tag)

a, b, c = "abc"
print(a)

zahlen =[10,18,12,15,90,10]
elf, *andere, zehn = zahlen
print(andere)

# Immutable != unveränderlich
a = ([],)
a[0].append("Test")
print(a)
