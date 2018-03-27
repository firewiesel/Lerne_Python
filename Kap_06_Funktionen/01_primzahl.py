#! /usr/bin/env python3

#---------------------------------------------------------------------------------------------------
# Dateiname: 
# Version: 
# Funktion:
# Autor:
# Erstellt am:
# Datum letzte Änderung:
#---------------------------------------------------------------------------------------------------

def primzahl (zahl):
    if zahl <=2:
        prim = False
    else:
        for i in range(2, zahl // 2):
            if zahl % i == 0:           # Teiler gefunden
                prim = False
                break
            else:
                prim = True
    return prim