#! /usr/bin/env python3

#08_grossbuchstaben.py

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for a in alphabet:
    for b in alphabet:
        print(a + b, end=" ")
print()