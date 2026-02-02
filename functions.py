def greet(name):
    print("Hallo,", name,"!")


def square(x):
    y = x**2
    print(y)


def rate(points):
    if points >= 60:
        return "Bestanden! Punkte:", points
    else:
        return "Nicht bestanden! Punkte:", points


def grade(schueler):
    for person in schueler:
        name = person["name"]
        points = person["punkte"]
        result = rate(points)
        print(name + ":", result)
        

greet("Chris")
greet("Paula")

square(3)

rate(85)
rate(55)

schueler = [{"name": "Anna", "punkte": 85}, {"name": "Ben", "punkte": 55}, {"name": "Clara", "punkte": 92}]
grade(schueler)
