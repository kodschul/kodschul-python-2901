# Python-Tupel Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Tupel-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Tupeln in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Erstellung und Zugriff auf ein Tupel

```python
# Erstellung und Zugriff auf ein Tupel
punkte = (3, 5)

# Zugriff auf einzelne Elemente
x_koordinate = punkte[0]
y_koordinate = punkte[1]

print("X-Koordinate:", x_koordinate)
print("Y-Koordinate:", y_koordinate)
```

## Beispiel 2: Unveränderlichkeit von Tupeln


```python
# Unveränderlichkeit von Tupeln
koordinaten = (1, 2)

# Dies führt zu einem Fehler
# koordinaten[0] = 5
```

## Beispiel 3: Verwendung von Tupeln in Funktionen


```python
# Verwendung von Tupeln in Funktionen
def rechteck_abmessungen(laenge, breite):
    flaeche = laenge * breite
    umfang = 2 * (laenge + breite)
    return flaeche, umfang

abmessungen = rechteck_abmessungen(4, 5)

print("Fläche und Umfang:", abmessungen)
```

## Beispiel 4: Tupelentpackung


```python
# Tupelentpackung
position = (10, 20, 30)

x, y, z = position

print("X-Position:", x)
print("Y-Position:", y)
print("Z-Position:", z)
```