#! /usr/bin/env python3

#alter.py

print("Bitte geben Sie ihr Alter ein.")
alter = input("Alter: ")
if 14 <= int(alter) < 18:
    print("Sie sind ein Jungendlicher.")
else:
    print("Sie sind ein Erwachsener.")