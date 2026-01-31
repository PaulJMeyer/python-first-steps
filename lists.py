shopping = ["banana", "shampoo", "cereals", "tea", "napkins", "coffee", "chocolate"]

count = 0
for _ in shopping:
    count += 1

print("Items counted:", count)

print("Number of items on the list:", len(shopping))
print ("First and last item form the shopping list:", shopping[0], shopping[-1])

numbers = [3, 12, 5, 8, 20, 1, 7]
highnumbers = []


for _ in numbers:
    if _ > 5:
        highnumbers.append(_)

double = []

for _ in numbers:
    double.append(_ * 2)

print("\nList contains following numbers:", numbers)
print ("Numbers > than 5:", highnumbers)
print("List with doubled numbers:", double)

#Ich habe die Aufgaben 1-6 abgeschlossen.