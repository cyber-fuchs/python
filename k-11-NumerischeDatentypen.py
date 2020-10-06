# Datentypen: int, float, bool, complex

x=7; y=4
print(x//y) # oder runden(x/y)
print(x%y)  # oder x-y*runden(x/y)
print (x, " / ",y," = ",x//y," Rest",x%y)

x+=y # x=x+y
x-=y # x=x-y
x*=y # x=x*y
print(x)

#Konvertierungen
x = 33.0
print(x)

x=int(33.5)
print(x)

x=bool(12)
print(x)

x = complex(True)
print(x)

#Bitweise 
x=107;y=25
print(x&y)

#   107 =   0110 1011
#    25 =   0001 1001
#   -----------------
#           0000 1001 = 9

print(x|y)
#   107 =   0110 1011
#    25 =   0001 1001
#   -----------------
#           0111 1011 = 123

#Bit-Shift
print(x<<1)
#   107 =   0110 1011
#   <<1     1101 0110

print(x>>1)
#   107 =   0110 1011
#   >>1     0011 0101 | 1 <- entfällt

print(x.bit_length())

a=True
if a or print("Lazy"):
    print("Evaluation")
    