#Aufgabe 1:
x = 7

if x % 2 == 0:
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")

#Aufgabe 2:
value = 150

if value < 100:
    print("Die Zahl ist kleiner als 100.")
elif value == 100:
    print("Die Zahl ist 100.")
else:
    print("Die Zahl ist größer als 100.")

#Aufgabe 3:
password = "python123"

if len(password) >= 8:
    print("Gültiges Passwort.")
else:
    print("Das Passwort ist zu kurz.")

#Aufgabe 4:
temp = 25

if temp < 10:
    print("kalt")
elif 10 <= temp <= 25:
    print("angenehm")
else:
    print("heiß")

#Aufgabe 5:
value = 15

if isinstance(value, int):
    if value > 10:
        print("große ganze Zahl")
    else:
        print("kleine ganze Zahl")    
elif isinstance(value, float):
    print("Kommazahl")
else:
    print("anderer Typ")