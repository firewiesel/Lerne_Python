#! /usr/bin/env python3

#11_trainer.py

import random
import time

print("Multiplikationstrainer")
print("----------------------")

startzeit = time.time()

for i in range(5):
    a = random.randint(1, 20)
    b = random.randint(1, 10)
    ergebnis = -1
    while ergebnis != a * b:
        ergebnis = int(input(str(a) + "*" + str(b) + "="))
        if ergebnis == a * b:
            print("Richtig!")
        else:
            print("Falsch! Versuchen Sie es noch einmal")
zeit = int(time.time() - startzeit)
print("Für die Aufgabe haben Sie", zeit, "Sekunden benötigt.")