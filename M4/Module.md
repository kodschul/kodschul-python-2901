# Python-Module Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Module-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Modulen in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Importieren von Modulen

```python
# Importieren von Modulen
import math

# Verwendung von Funktionen aus dem Modul
wurzel = math.sqrt(9)
print("Quadratwurzel von 9:", wurzel)
```

## Beispiel 2: Benennung bei Import

```python
# Benennung bei Import
import random as zufall

# Verwendung von Funktionen mit neuer Bezeichnung
zufallszahl = zufall.randint(1, 10)
print("Zufallszahl zwischen 1 und 10:", zufallszahl)
```

## Beispiel 3: Eigene Module erstellen

```python
# Eigene Module erstellen
# Modul: rechner.py

def addiere(a, b):
    return a + b

def subtrahiere(a, b):
    return a - b
```

## Beispiel 4: Verwenden eigener Module

```python
# Verwenden eigener Module
# Hauptprogramm: main.py
import rechner

ergebnis1 = rechner.addiere(5, 3)
ergebnis2 = rechner.subtrahiere(10, 4)

print("Summe von 5 und 3:", ergebnis1)
print("Differenz von 10 und 4:", ergebnis2)
```

## Beispiel 5: Selektives Importieren von Modulobjekten

```python
# Selektives Importieren von Modulobjekten
from math import sqrt

# Verwendung des direkt importierten Objekts
wurzel = sqrt(16)
print("Quadratwurzel von 16:", wurzel)
```

## Beispiel 6: Importieren aller Objekte aus einem Modul

```python
# Importieren aller Objekte aus einem Modul
from random import *

# Verwendung aller Funktionen des Moduls ohne Modulpräfix
zufallszahl = randint(1, 100)
print("Zufallszahl zwischen 1 und 100:", zufallszahl)
```

## Beispiel 7: Importieren von eigenen lokalen Modulen

```python
# Importieren von eigenen lokalen Modulen
from meine_module import eigene_funktion

# Verwendung der importierten Funktion
ergebnis = eigene_funktion()
print("Ergebnis der eigenen Funktion:", ergebnis)
```

## Beispiel 8: Importieren von Modulen aus Unterverzeichnissen

```python
# Importieren von Modulen aus Unterverzeichnissen
from unterverzeichnis.mein_modul import meine_funktion

# Verwendung der importierten Funktion
ergebnis = meine_funktion()
print("Ergebnis der Funktion aus Unterverzeichnis:", ergebnis)
```