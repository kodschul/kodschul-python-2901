# Python-Fehlermeldungen Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Fehlermeldungen-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Fehlermeldungen in Python kennenlernen und wie Sie diese lesen und interpretieren können. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 0: Syntaxfehler

```python
# Syntaxfehler
print("Hallo Welt"
```

```python
# Indentationsfehler
def meine_funktion():
print("Diese Zeile gehört nicht zur Funktion.")
```

```python
# NameError
print(variable)
```

```python
# TypeError
zahl = "10"
ergebnis = zahl + 5
```

```python
# FileNotFoundError
datei = open("nicht_vorhanden.txt", "r")
inhalt = datei.read()
datei.close()
```

## Beispiel 1: Einfache Exception

```python
# Einfache Exception
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 10 / zahl
    print("Ergebnis:", ergebnis)

except Exception as e:
    print(f"Fehler: {e}")
```

## Beispiel 2: Mehrere Exceptions abfangen

```python
# Mehrere Exceptions abfangen
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 10 / zahl
    print("Ergebnis:", ergebnis)

except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")

except ValueError:
    print("Fehler: Ungültige Eingabe. Bitte geben Sie eine Zahl ein.")
```

## Beispiel 3: Eigene Exception-Klasse erstellen

```python
# Eigene Exception-Klasse erstellen
class MeinFehler(Exception):
    pass

try:
    raise MeinFehler("Dies ist meine eigene Exception.")
except MeinFehler as e:
    print(f"Abgefangene Exception: {e}")

```

## Beispiel 4: Finally-Block mit Exception

```python
# Finally-Block mit Exception
try:
    zahl = int(input("Geben Sie eine Zahl ein: "))
    ergebnis = 10 / zahl
    print("Ergebnis:", ergebnis)

except ZeroDivisionError:
    print("Fehler: Division durch Null ist nicht erlaubt.")

finally:
    print("Finally-Block wird immer ausgeführt, unabhängig von Fehlern.")

```