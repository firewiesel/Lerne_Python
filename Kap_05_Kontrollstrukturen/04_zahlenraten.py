#! /usr/bin/env python3

#zahlenraten.py
import random

zufahlszahl = random.randint(0, 100)
print("Raten Sie eine Zahl: ")
zahl = -1
while zahl != zufahlszahl:
    zahl = int(input("Zahl: "))
    if zahl == zufahlszahl:
        print("Sie haben die Zahl gefunden.")
    elif zahl < zufahlszahl:
        print("Zahl zu klein!")
    else:
        print("Zahl zu gross!")