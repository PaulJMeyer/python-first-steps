#Aufgabe 1:
letters = {"A", "C", "G", "T"}

print(letters)

#Aufgabe 2: in Set umwandeln / Duplikate entfernen
letters = ["A", "C", "A", "G", "T", "A"]

letters_set = set(letters)
print(letters_set)

#Aufgabe 3: ist A Teil des Sets?
if "A" in letters_set:
    print("A ist Teil des Sets.")

#Aufgabe 4: gemeinsame Elemente finden.
set1 = {"A", "C", "G"}
set2 = {"G", "T", "A"}
# set3 = set()

# for letter in set1:
#     if letter in set2:
#         set3.add(letter)
#Einfachere Variante:
set3 = set1 & set2

print(set3)

#Aufgabe 5: Elemente finden, die nur in set1 sind
# set4 = set()

# for letter in set1:
#     if not letter in set2:
#         set4.add(letter)
#Einfachere Variante:
set4 = set1 - set2

print(set4)