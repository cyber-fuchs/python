import time
import datetime

t = time.struct_time((2007,9,10,18,24,56,0,0,0))
print(t)
print("Wie heißt meine Timezone?",time.tzname)

t = time.asctime()
print("Systemzeit:",t)
t = time.asctime((1987,7,26,10,40,0,0,0,0))
print(t)

# Counter
# start = time.perf_counter()
# rechenintensiv = 999999 ** 1234563
# ende = time.perf_counter()
# print("Die Function lief: {:1.2f} Sekunden".format(ende - start))

t = time.gmtime()
print(t)

t1 = time.localtime()
t2 = time.localtime(time.mktime(t1))
print(t1)

t = time.strftime("%d.%m.%Y um %H:%M:%S Uhr")
print(t)

#Aus einem String eine Zeit-Variable machen
zeit_string = "23.10.2020 um 06:22:35 Uhr"
t = time.strptime(zeit_string, "%d.%m.%Y um %H:%M:%S Uhr")
print(t)

print("Unix-TimeStamp:", time.time())

t = datetime.date(1995,8,2)
print(t)

# Zeit bis zur Bescherung
bescherung = datetime.datetime(2020,12,24,18,30)
ausgabe = bescherung - datetime.datetime.now()
print(f"Es sind noch {ausgabe.days} Tage und {ausgabe.seconds / 3600:1.0f} Stunden bis zur Bescherung")


#print(f"{ausgabe.days} Tage und {ausgabe.hour} Stunden")
# Gewünschte Ausgabe: 62 Tage und 11 Stunden und 26 Minuten
