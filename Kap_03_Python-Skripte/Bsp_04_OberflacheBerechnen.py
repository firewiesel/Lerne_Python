#! /usr/bin/env python3

# Berechnung der Oberfläche eines Quaders


länge = 6
breite = 2
höhe = 3

oberfläche = 2 * (
    breite * höhe       # Vorder- und Rückseite
    + länge * breite    # Ober- und Unterseite
    + länge * höhe      # rechte und linke Seite
    )

print(oberfläche)
