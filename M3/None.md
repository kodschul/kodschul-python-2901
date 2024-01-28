# Python-None Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-None-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von `None` in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Verwendung von None

```python
# Verwendung von None
ergebnis = None

if ergebnis is None:
    print("Das Ergebnis ist nicht definiert.")
else:
    print("Das Ergebnis ist:", ergebnis)
```

## Beispiel 2: Funktionen ohne Rückgabewert

```python
# Funktionen ohne Rückgabewert
def einfache_funktion():
    print("Diese Funktion hat keinen Rückgabewert.")

ergebnis = einfache_funktion()

if ergebnis is None:
    print("Die Funktion gibt None zurück.")
```

## Beispiel 3: Initialisierung von Variablen

```python
# Initialisierung von Variablen mit None
name = None

if name is None:
    name = input("Bitte geben Sie Ihren Namen ein: ")

print("Hallo,", name)
```

## Beispiel 4: Überprüfung auf None

```python
# Überprüfung auf None
liste = [1, 2, 3]
element = liste.pop()

if element is not None:
    print("Das entfernte Element ist:", element)
else:
    print("Die Liste ist leer.")
```