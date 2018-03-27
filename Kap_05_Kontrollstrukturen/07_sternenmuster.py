#! /usr/bin/env python3

#07_sternenmuster.py

# drei Zeilen mit je 4 Sternen
for i in range(3):
    print("* * * *")

# Sterndreieck
for i in range(5):
    print((i + 1) * "* ")

# Sternendreieck 2
for i in range(4):
    print((3 - 1) * " ",(2 * i + 1) * "* ")
