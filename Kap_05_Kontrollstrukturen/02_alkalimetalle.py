#! /usr/bin/env python3

#alaklimetalle.py

print("Bitte geben Sie das Symbol eines Alkalimetalls an:")
element = input("Element: ")
if element in ["Li", "Na", "K", "Rb", "Cs"]:
    print("Es handlet sich um ein Alkalimetall")
else:
    print("Es handlet sich um KEIN Alakalimetall")
input("Mit ENTER beenden ")