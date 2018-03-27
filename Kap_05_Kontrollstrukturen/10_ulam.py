#! /usr/bin/env python3

#10_ulam.py

print("Berechnung der (3a + 1)-Folge von Ulam")

a = int(input("Startwert: "))

while a != 1:
    print(a)
    if a % 2 == 0:
        a = a / 2
    else:
        a = 3 * a + 1
print(a)
