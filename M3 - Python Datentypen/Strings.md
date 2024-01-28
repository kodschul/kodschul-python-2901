# Python-Strings Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-String-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Strings in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Erstellung und Zugriff auf einen String

```python
# Erstellung und Zugriff auf einen String
text = "Hallo, Python!"

# Zugriff auf einzelne Zeichen
erstes_zeichen = text[0]
letztes_zeichen = text[-1]

print("Erstes Zeichen:", erstes_zeichen)
print("Letztes Zeichen:", letztes_zeichen)
```

## Beispiel 2: String-Operationen

```python
# String-Operationen
vorname = "Max"
nachname = "Mustermann"

# Konkatenation von Strings
voller_name = vorname + " " + nachname

# Wiederholung von Strings
gruss = "Hallo! " * 3

print("Voller Name:", voller_name)
print("Gruß:", gruss)
```

## Beispiel 3: String-Methoden

```python
# String-Methoden
text = "Hallo, Python!"

# Umwandlung in Großbuchstaben
großbuchstaben = text.upper()

# Aufteilen des Strings
woerter = text.split(", ")

print("In Großbuchstaben:", großbuchstaben)
print("Aufgeteilte Wörter:", woerter)
```

## Beispiel 4: Formatierung von Strings

```python
# Formatierung von Strings
alter = 25
name = "Max"

text = "Mein Name ist {} und ich bin {} Jahre alt.".format(name, alter)

print(text)
```