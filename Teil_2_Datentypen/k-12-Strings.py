# Kapitel 12 - Strings
print("---Kapitel 12 Strings---")
print("---Steuerzeichen---")
a="Erste Zeile\nZeite Zeile"
print(a)

# \a - Bell / \b Backspace / \t - Tabulator / \n - new Line ...

print("---STring-Methoden---")

# s.split
print("Methode s.split([sep,maxsplit]) und s.rsplit")
s = "1-2-3-4-5-6-7-8-9-0"
print(s)
print(s.split("-"))
print(s.split("-",5))
print(s.rsplit("-",5))

s = "1---3-4-5"
print(s)
print(s.split("-"))
