# shopping = ["banana", "shampoo", "cereals", "tea", "napkins", "coffee", "chocolate"]

# count = 0
# for _ in shopping:
#     count += 1

# print("Items counted:", count)

# print("Number of items on the list:", len(shopping))
# print ("First and last item form the shopping list:", shopping[0], shopping[-1])

# numbers = [3, 12, 5, 8, 20, 1, 7]
# highnumbers = []


# for _ in numbers:
#     if _ > 5:
#         highnumbers.append(_)

# double = []

# for _ in numbers:
#     double.append(_ * 2)

# print("\nList contains following numbers:", numbers)
# print ("Numbers > than 5:", highnumbers)
# print("List with doubled numbers:", double)

#Aufgabe 1:
numbers = [1, 2, 3]

numbers.extend([4, 5])
print(numbers)

#Aufgabe 2:
letters = ["A", "C", "G", "T"]

print(letters[0], letters[-1])      # -1 = letztes Element

#Aufgabe 3:
numbers = [4, 17, 2, 9, 12]
highest_number = numbers[0]

for key in numbers:
    if key > highest_number:
        highest_number = key

print(highest_number)

#Aufgabe 4:
numbers = [3, 12, 7, 18, 5, 20]
filtered = []   #neue Liste ist wichtig. Wenn man Elemente aus Listen entfernt, können diese in loops übersprungen werden.

for key in numbers:
    if key > 10:
        filtered.append(key)
# eleganter (list comprehension):
filtered = [number for number in numbers if number > 10]

print(filtered)

#Aufgabe 5:
numbers = []

for i in range(0,9):
    if i % 2 == 0:
        numbers.append(i)

print(numbers)