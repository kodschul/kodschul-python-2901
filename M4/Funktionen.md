# Python-Funktionen Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Funktions-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Funktionen in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Einfache Funktion

```python
# Einfache Funktion
def gruss():
    print("Hallo! Herzlich willkommen.")

# Aufruf der Funktion
gruss()
```

## Beispiel 2: Funktionen mit Parametern

```python
# Einfache Funktion
def gruss():
    print("Hallo! Herzlich willkommen.")

# Aufruf der Funktion
gruss()
```

## Beispiel 3: Rückgabewerte

```python
# Funktion mit Rückgabewert
def quadrat(zahl):
    return zahl ** 2

# Aufruf der Funktion und Verwendung des Rückgabewerts
ergebnis = quadrat(4)
print("Quadrat von 4:", ergebnis)
```

## Beispiel 4: Funktionen mit Standardwerten

```python
# Funktionen mit Standardwerten
def multipliziere(a, b=2):
    return a * b

# Aufruf der Funktion mit einem oder beiden Argumenten
ergebnis1 = multipliziere(3)
ergebnis2 = multipliziere(3, 4)

print("Ergebnis mit einem Argument:", ergebnis1)
print("Ergebnis mit beiden Argumenten:", ergebnis2)
```

## Beispiel 5: Funktionen mit variabler Anzahl von Parametern

```python
# Funktionen mit variabler Anzahl von Parametern
def summe(*zahlen):
    ergebnis = 0
    for zahl in zahlen:
        ergebnis += zahl
    return ergebnis

# Aufruf der Funktion mit verschiedenen Anzahlen von Argumenten
ergebnis1 = summe(1, 2, 3)
ergebnis2 = summe(4, 5, 6, 7)

print("Summe von 1, 2, 3:", ergebnis1)
print("Summe von 4, 5, 6, 7:", ergebnis2)
```

## Beispiel 6: Lambda-Funktionen

```python
# Lambda-Funktionen (anonyme Funktionen)
quadrat = lambda x: x**2

# Aufruf der Lambda-Funktion
ergebnis = quadrat(5)
print("Quadrat von 5:", ergebnis)
```

## Beispiel 7: Funktionen als Parameter

```python
# Funktionen als Parameter übergeben
def anwenden_operation(a, b, operation):
    return operation(a, b)

# Definition von Operationen als separate Funktionen
def addition(x, y):
    return x + y

def multiplikation(x, y):
    return x * y

# Anwendung der Funktion mit verschiedenen Operationen
ergebnis1 = anwenden_operation(3, 4, addition)
ergebnis2 = anwenden_operation(3, 4, multiplikation)

print("Addition von 3 und 4:", ergebnis1)
print("Multiplikation von 3 und 4:", ergebnis2)
```
