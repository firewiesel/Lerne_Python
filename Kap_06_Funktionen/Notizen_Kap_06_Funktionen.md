# Notizen zu Kap 06 Funktionen
Funktionen können wiederkehrende Aufgaben schrittweise Verfeinern und stellen Rekursionen sicher.


## Was ist Rekursion
Rekursive Funktionen sind Funktionen die sich selber aufrufen. Der Aufruf geschieht mit anderen
Argumenten.

## Generelles über Funktionen
Funktion werden in Python Programmen meistens aufgerufen. Es können aber auch eigene Funktionen 
definiert werden.

### Funktionsaufruf
```python
    function (parameterliste)
```

### Funktionsdefinition
```python
def funktionsname (parameterlsite):
    """ (Docstring) Knappe Beschreibung der Funktion

    - Vorbedingungen
    - Nachbedingungen
    - welche globalen Variablen werden verwendet
    - Name Autor und wann geändert
    """
    anweisungsblock
```

### Allgemeiens Verfahren Programmdefinition
Ein Aufgabe wird in Teilaufgaben unteteilt. Diese Aufteilung besteht aus dem EVA Prinzip:
- Eingabe
- Ausgabe
- Verarbeitung

Python Skripte bestehen im Prinzip aus zwei Teilen:
- benötigte Funktionen definieren
- Hauptprogramm, das die defineirten Funktionen aufruft