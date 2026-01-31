import random

percent = random.randint(0, 101)

print("Es wurden", percent, "% der möglichen Punkte erreicht.")

if percent >= 95:
    print("Das entspricht der Note 1,0 (1).")
elif 95 > percent >= 90:
    print("Das entspricht der Note 1,3 (1-).")
elif 90 > percent >= 85:
    print("Das entspricht der Note 1,7 (2+).")
elif 85 > percent >= 80:
    print("Das entspricht der Note 2,0 (2).")
elif 80 > percent >= 75:
    print("Das entspricht der Note 2,3 (2-).")
elif 75 > percent >= 70:
    print("Das entspricht der Note 2,7 (3+).")
elif 70 > percent >= 65:
    print("Das entspricht der Note 3,0 (3).")
elif 65 > percent >= 60:
    print("Das entspricht der Note 3,3 (3-).")
elif 60 > percent >= 55:
    print("Das entspricht der Note 3,7 (4+).")
elif 55 > percent >= 50:
    print("Das entspricht der Note 4,0 (4).")
else:
    print("Das entspricht der Note 5,0 (5).")