#! /usr/bin/env python3

#03_schaltjahre.py

jahr = int(input("Geben Sie ein Jahr ein: "))
if (jahr%400 == 0) or (jahr%4 == 0) and not (jahr%100 == 0):
    print("Es ist ein Schaltjahr!")
else:
    print("Es ist KEIN Schaltjahr!!!")
input("Eingabe mit ENTER beenden.")