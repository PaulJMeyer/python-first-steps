# profile = {"name": "Paul","age": "29","profession": "molecular biologist"}

# print("Pauls profile:")
# for key, value in profile.items():
#     print(f"{key}: {value}")

# grades = {"Anna": 1.7, "Ben": 2.3, "Clara": 1.3, "Paula": 1.0}

# print("Only Bens grade:")
# for key, value in grades.items():
#     if key == "Ben":
#         print(f"{key}: {value}")
    
# print("All names:")
# for key, value in grades.items():
#     print(f"{key}")

#Aufgabe 1:
person = {
    "name": "Paul",
    "age": 30,
    "city": "Bremen"
}
print(person["name"])

#Aufgabe 2:
person["job"] = "Biologist"
print(person)

#Aufgabe 3:
person = {
    "name": "Paul",
    "age": 30,
    "city": "Bremen"
}

for key, value in person.items():       #key/value unpacking
    print(f"{key} {value}")

#Aufgabe 4:

if "age" in person:
    print(f"Das Alter ist: {person["age"]}")

#Aufgabe 5:
letters = ["A", "C", "A", "G", "T", "A", "C"]
letters_dict = {}

for letter in letters:
    if letter in letters_dict:
        letters_dict[letter] += 1
    else:
        letters_dict[letter] = 1

print(letters_dict)