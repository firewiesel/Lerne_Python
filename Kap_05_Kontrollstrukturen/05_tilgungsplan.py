#! /usr/bin/env python3

#05_tilgungsplan.py
print("Berechnung des Tilgungsplans für einen Kredit")
print()

schulden = float(input("Kreditsumme: "))
zinssatz = float(input("Zinsatz (Prozent pro Jahr): "))
rueckzahlung = float(input("Jährliche Rückzahlung: "))
jahr = 2003

while schulden > rueckzahlung:
    zinsen = schulden * zinssatz / 100
    tilgung = rueckzahlung - zinsen
    schulden = schulden - tilgung
    jahr += 1
    print(jahr, " Zinsen: ", zinsen, "EUR", " Tilgung:", tilgung, "EUR", " Restschulden", schulden, "EUR")

print("Restforderung;" , schulden, "EUR")