# Aufgabe 1
a = 5
b = 3.14
c = "Hallo"
d = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))

# Aufgabe 2
x = 10
y = "10"

print(type(x))
print(type(y))
print("Are x and y of the same type?", type(x) == type(y))

# Aufgabe 3
zahl_str = "25"
zahl_int = int(zahl_str)
zahl_float = float(zahl_str)

print(f"{zahl_int} ({type(zahl_int)}), {zahl_float} ({type(zahl_float)})")

# Aufgabe 4
alter = 30
print(f"Ich bin {alter} Jahre alt.")

#Aufgabe 5 (int, float, str?)
value = 3.14

if isinstance(value, int):
    print("The value type is int.")
elif isinstance(value, float):
    print("The value type is float.")
elif isinstance(value, str):
    print("The value type is str.")
else:
    print("The value type is other than int, float, str.")

#Aufgabe Bonus:
x = "5"
y = 5

x = int(x)

print(x + y)