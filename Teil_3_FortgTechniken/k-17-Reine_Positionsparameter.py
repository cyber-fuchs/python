print("Kapitel 17 - Reine Positionsparameter".center(50, "-"))


def f(a, b, /, c, d):
    print(a, b, c, d)


# f(1,b=2, c=3, d=4)
f(1, 2, c=3, d=4)

print("\n" + "17.3.6 Entpacken einer Parameterliste".center(50, "-"))


def summe(*parameter):
    s = 0
    for p in parameter:
        s = s + p
    return s


t = (1, 4, 3, 7, 9, 2)
print(summe(t[0], t[1], t[2], t[3], t[4], t[5]))

print(*range(11))
print(summe(*range(101)))
print(summe(*t))

dict = {"a": 7, "b": 3, "c": 9}
# print(summe( **dict ))
print(summe(*(1, 2), *(3, 4)))

def f(a,b):
    print(id(a))
    print(id(b))

p = 1
q = [1,2,3]
print(id(p))
print(id(q))
f(p,q)

print("\n"+"Veränderungen durch Funktionen verhindern")
def foo(liste):
    liste[0]=32
    liste += [5,6,7,8]

zahlen = [1,2,3,4]
foo(zahlen)
print(zahlen)

safe = [1,2,3,4]
foo(safe[:])
print(safe)
