# def greet(name):
#     print("Hallo,", name,"!")


# def square(x):
#     y = x**2
#     print(y)


# def rate(points):
#     if points >= 60:
#         return "Bestanden! Punkte:", points
#     else:
#         return "Nicht bestanden! Punkte:", points


# def grade(schueler):
#     for person in schueler:
#         name = person["name"]
#         points = person["punkte"]
#         result = rate(points)
#         print(name + ":", result)
        

# greet("Chris")
# greet("Paula")

# square(3)

# print(rate(85))
# print(rate(55))

# schueler = [{"name": "Anna", "punkte": 85}, {"name": "Ben", "punkte": 55}, {"name": "Clara", "punkte": 92}]
# grade(schueler)

#Aufgabe 1: x²
def square(x):
    return x**2

print(square(3))
print(square(5))

#Aufgabe 2: Maximum einer Liste ausgeben
numbers = [2, -12, 0, 25, 10, -7]

def find_max(numbers):
    highest_number = numbers[0]
    for number in numbers:
        if number > highest_number:
            highest_number = number
    return highest_number

print(find_max(numbers))

#Aufgabe 3: ein dict mit Häufigkeiten widergeben
letters = ["A", "C", "A", "G", "T", "A", "C"]

def count_letters(letters):
    letters_dict = {}
    for letter in letters:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

print(count_letters(letters))

#Aufgabe 4: Liste filtern
numbers = [2, -12, 0, 25, 10, -7]

def filter_greater_than(numbers, threshold):
    numbers_filtered = [number for number in numbers if number > threshold]
    return numbers_filtered

print(filter_greater_than(numbers, 0))

#Aufgabe 5: GC content berechnen

# def gc_content(sequence):
#     counter = 0
#     for base in sequence:
#         if base == "G" or base == "C":
#             counter += 1
#     return float(counter / len(sequence) * 100)

#kürzerer, sauberer:
def gc_content(sequence):
    seq = sequence.upper()
    gc = sum(1 for base in seq if base in ("G", "C"))
    return gc / len(seq) * 100.0

print(gc_content("AGCGATCGATCTGATGCGT"))