print("Funktionsparameter".center(40,"-"))
print("Beliebige Anzahl von Parameter".center(40,"-"))
def funktion(a,b,*weitere):
    print("Feste Parameter", a,b)
    print("Weitere Parameter", weitere)

funktion(1,2,"Hallo Welt",4,5)

def summe(*parameter):
    s = 0
    for p in parameter:
        s += p
    return s

print(summe(18,19,20,21,22))

def funktion2(a,b,**weitere):
    print("Feste Parameter", a,b)
    print("Weitere Parameter", weitere)

funktion2(1,2,auto="Mercedes",model="e220")

print("Reine Schlüsselwortparameter".center(40,"-"))
def f(a, b, *c, d, e):
    print(a,b,c,d,e)

f(1,2,3,d=4,e=5)

def f1(a, b, *args, d, e, **kwargs):
    print(a,b,args,d,e,kwargs)

f1(1,2,3,d=4,e=5)