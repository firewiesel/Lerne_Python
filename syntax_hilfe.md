# Syntax Hilfen
Hier sind einige Syntaxhilfen zur Python Programmiersprache aufgelistet.

## Schlüsselwörter _(keywords)_
    False   class       finally     is          return
    None    continue    for         lambda      try
    True    def         from        nonlocal    while
    and     del         global      not         with
    as      elif        if          or          yield
    assert  else        import      pass
    breack  except      in          raise

## Standarobjekte Abfragen
* Objekttyp ermitteln
    ```python
    type()
    ```

* Identität abfragen
    ```python
    id()
    ```
## Allgemein Syntax Namen für Bezeichner
Ein Bezeichner beginnt immer mit einem Buchstaben oder Unterstrich `_` .

Es dürfen noch ganze Zahlen in einem Bezeichner stehen.

Sonderzeichen, wie `?, $, !...` sind nicht erlaubt!

## Explizites Verbinden von Zeilen
Mit dem Zeichen \ (Backslash) können mehrere Zeilen miteinander verbunden werde.

Beispiel:
```python
import time

print("Die aktuelle \
Uhrzeit")
print(time.asctime())
```

> Hinter dem \ Backslash darf nichts mehr stehen. Auch Kommentare dürfen nicht hinter dem \ 
Backslash stehen!


## Guter Programmierstil

_Guter Programmierstil_ bezeichnt die Kunst des Einrückens und des Kommentierens.

Damit ist der Code für alle, auch für die Person welche den Code schreibt, auch noch nach Jahren
besser lesbar.

Der Aufwand mag am Anfang gross sein, er zahlt sich aber mit der Zeit aus.

### Bezeichnerwahl
Der Name von Bezichnern sollte die Bedeutung für das Vorhanben/ Funkktion repräsentieren.

```python
länge = input("Länge des Quadrats in cm: ")
l = int(länge)
breite = input("Breite des Quadrats in cm: ")
b = int(breite)
höhe = input("Höhe des Quadrats in cm: ")
h = int(höhe)

volumen = l * b * h
print("Das Voulumen ist", volumen, "Kubikzentimeter")
```

Variablen, Funktion und Methoden werden in Python _immer_ klein geschrieben!

Die Namen von Klassen werden im Gegensatz _immer_ gross geschrieben.
 
### Layout
Jede Anweisung sollte in einer neuen Zeile stehen. Dies hilft der Übersicht des Programms.

Lange Skripte sollten (nach ca. mehr als 10 Zeilen) durch sinnvolle Abschnitte unterteilt werden.

### Kommentare
Bei grösseren Projekte sollte am Anfang immer ein Kommentar stehen, welche die Funktion, die Version,
der Autor... beschreibt.

Beispiel:
```python
#! /usr/local/bin/python3

#---------------------------------------------------------------------------------------------------
# Dateiname: 
# Version: 
# Funktion:
# Autor:
# Erstellt am:
# Datum letzte Änderung:
#---------------------------------------------------------------------------------------------------
```

Kommentare sollte man während der Programmierung schreiben, nicht erst nachträglich!