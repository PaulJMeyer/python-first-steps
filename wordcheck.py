word = "pythoooooon"

length = 0

for base in word:
    length += 1

print("Buchstaben im Wort:", length)

if length > 10:
    print("Das Wort ist lang (>10).")
elif 10 >= length > 4:
    print("Das Wort ist mäßig lang (4-10).")
else:
    print("Das Wort ist kurz (<4).")