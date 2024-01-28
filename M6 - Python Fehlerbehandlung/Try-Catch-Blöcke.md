# Python-Try-Catch-Blöcke Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Try-Catch-Blöcke-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Try-Catch-Blöcken (auch Exception Handling genannt) in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Einfacher Try-Catch-Block

```python
# Einfacher Try-Catch-Block
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 10 / zahl
    print("Ergebnis:", ergebnis)

except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")

except ValueError:
    print("Fehler: Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
```

## Beispiel 2: Verwendung des generischen Exception-Blocks

```python
# Verwendung des generischen Exception-Blocks
try:
    datei = open("nicht_vorhanden.txt", "r")
    inhalt = datei.read()
    datei.close()

except Exception as e:
    print(f"Fehler: {e}")
```

## Beispiel 3: Try-Catch mit else-Zweig

```python
# Try-Catch mit else-Zweig
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    quadrat = zahl ** 2

except ValueError:
    print("Fehler: Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")

else:
    print("Das Quadrat der Zahl ist:", quadrat)
```

## Beispiel 4: Finally-Block

```python
# Finally-Block
try:
    datei = open("beispiel.txt", "r")
    inhalt = datei.read()

except FileNotFoundError:
    print("Fehler: Datei nicht gefunden.")

finally:
    print("Finally-Block wird immer ausgeführt, unabhängig von Fehlern.")
    if 'datei' in locals():
        datei.close()
```