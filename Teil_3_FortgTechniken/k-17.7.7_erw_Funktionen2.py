print("Kapitel 17.7.7 Bytearray".center(50,"-"))
import binascii
b_var = bytearray("äüö","utf-8")
print("äüö in Bytes?:")
print(b_var)

b_var = bytearray([1,2,3,4])
print("1 2 3 4 in Bytes:")
print(b_var)
print("10 Bytes bitte:")
print(bytearray(10))
b2_var = 1337
print(f"1337 in binär: {b2_var:#b}")
print("\n" + "17.7.8 bytes".center(50,"-"))
print("Das sind 10 Bytes:", bytes(10))
print("äüö in Bytes",bytes("äüö","utf-8"))

print("\n" + "17.7.9 chr".center(50,"-"))
print(chr(12), chr(14), chr(216))

print("\n" + "17.7.11 dict (dictonary)".center(50,"-"))
print( dict({"a" : 1, "b" : 2}))

print("\n" + "17.7.13 enumerate".center(50,"-"))
for i, wert in enumerate([1,2,3,4,5]):
    print("Der Wert von iterable an", i, "ter Stelle ist", wert)

print("\n" + "17.7.14 eval".center(50,"-"))
print("2 + 2 = ",eval("2+2"),"und 12 hoch 2 ist",eval("12**2"))

print("\n" + "17.7.16 filter".center(50,"-"))
filterobj = filter(lambda x: x%2 == 0, range(21))
print(list(filterobj))

print("\n" + "17.7.23 filter".center(50,"-"))
print(hex(12), hex(0xFF))

print("\n" + "17.7.25 input".center(50,"-"))
#s = input("Geben Sie einen Text ein:")
#print(s)
#s = eval(input("Was wollen Sie berechnen?:"))
#print(s6

print("\n" + "17.7.25 int".center(50,"-"))
print("Was ist 0xFA ?:", int("FA",16), "=", int(hex(250),16))

