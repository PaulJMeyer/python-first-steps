import random
leben = 3
richtig = random.randint(1,10)
eingabe = int(input("Ich denke mir eine Zahl zwischen 1 und 10, errate sie!"))
while eingabe != richtig and leben > 1:
    leben -= 1
    print("Leben:", leben)
    if eingabe < richtig: 
        eingabe = int(input("Zu niedrig. Nochmal:"))
    else: 
        eingabe = int(input("Zu hoch. Nochmal:"))
if eingabe == richtig: print("Gewonnen!")
else: print ("Verloren! Die Zahl war:", richtig)
