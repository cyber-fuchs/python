print("Kapitel 17 - Namensräume".center(50, "-"))
print("nonlocal - Zugriff auf Funktionslokale Variablen")


def f1():
    def f2():
        nonlocal res
        res += 1

    res = 1
    f2()
    print(res)


f1()

name = "fuchs"


def hallo():
    print("Hallo " + name)


hallo()

print("\n" + "Anonyme Funktion lambda".center(50, "-"))
s = lambda x: -x
print(s(10))
out = sorted([1, 3, 8, 0, 2, 6, 7, 12], key=lambda x: -x)
print(out)

f = lambda x, y, z: (x - y) *z
print(f(8,3,4))
print((lambda x,y,z:(x-z)*z)(5,2,3))