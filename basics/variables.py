#Aufagbe 1:
x = 10
x += 5
print(x)

x *= 2
print(x)

#Aufgabe 2:
a = "Apfel"
b = "Banane"

a, b = b, a

print(f"a: {a}, b: {b}")

#Aufgabe 3:
name = "Paul"
city = "Bremen"
age = 30

print(f"{name} ist {age} Jahre alt und lebt in {city}.")

#Aufgabe 4:
PI = 3.14159
r = 4
area = PI * r**2
print(f"Area of a circle with r = 4 cm: {area:.2f} cm².")

#Aufgabe 5:
counter = 0

def increase(x):
    x += 1
    print (x)
    return (x)

increase(counter)
print(counter)
counter = increase(counter)
print(counter)