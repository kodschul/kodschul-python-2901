# Python-Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte und Syntax von Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Hallo Welt!

```python
print("Hallo Welt!")
```

## Beispiel 2: Variablen und Datentypen

```python
# Variablen
name = "Max"
alter = 25

# Datentypen
print(type(name))  # <class 'str'>
print(type(alter))  # <class 'int'>
```

## Beispiel 3: Bedingungen und Schleifen

```python
# Bedingungen
zahl = 10
if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl == 0:
    print("Die Zahl ist null.")
else:
    print("Die Zahl ist negativ.")

# Schleifen
for i in range(5):
    print(i)
```

## Beispiel 4: Funktionen

```python
# Funktionen
def addiere(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

ergebnis = addiere(3, 5)
print("Die Summe ist:", ergebnis)
```