#Aufgabe 1:
a = 15
b = 4

print(f"Summe: {a+b}, Differenz: {a-b}, Produkt: {a*b}, Quotient: {a/b}, Ganzzahlquotient: {a//b}, Rest: {a%b}, Potenzwert: {a**b}")

#Aufgabe 2:
x = 10
y = 20

print(f"Is x > y? {x>y}, Is x < y? {x<y}, Is x = y? {x==y}, Is x not equal to y? {x!=y}")

#Aufgabe 3:
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("Person darf eintreten.")
elif age >= 18 and has_ticket:
    print("Personen ohne Ticket dürfen nicht eintreten.")
elif age < 18 and has_ticket:
    print("Personen unter 18 dürfen nicht eintreten.")
else:
    print("Personen unter 18 und ohne Ticket dürfen nicht eintreten.")

#Aufgabe 4:
letters = ["A", "C", "G", "T"]

def letter_check(x):
    if "A" in x:
        print("A ist einer der Buchstaben.")
    else:
        print("A ist keiner der Buchstaben.")        
    if "B" in x:
        print("B ist einer der Buchstaben.")
    else:
        print("B ist keiner der Buchstaben.") 

letter_check(letters)

#Aufgabe 5:
value = 12

if 10 <= value <= 20:
    print("Die Zahl ist innerhalb des Bereichs.")
elif value < 10 or value > 20:
    print("Die Zahl ist außerhalb des Bereichs.")