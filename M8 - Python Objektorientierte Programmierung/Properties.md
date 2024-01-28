# Python-Properties Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Properties-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Properties in Python kennenlernen und wie sie verwendet werden können, um den Zugriff auf Attribute in Klassen zu steuern. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Einfache Property

```python
# Einfache Property
class Person:
    def __init__(self, name):
        self._name = name  # Privates Attribut

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 3:
            print("Der Name muss mindestens 3 Zeichen lang sein.")
        else:
            self._name = value

# Objekt erstellen
person1 = Person("Max")

# Lesen der Property
print("Name:", person1.name)

# Setzen der Property
person1.name = "Tom"

# Lesen der Property nach Änderung
print("Neuer Name:", person1.name)
```

## Beispiel 2: Read-only Property

```python
# Read-only Property
class Kreis:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

# Objekt erstellen
kreis1 = Kreis(5)

# Lesen der Property
print("Radius:", kreis1.radius)

# Versuch, die Property zu setzen (wird einen Fehler verursachen)
kreis1.radius = 8
```

## Beispiel 3: Property mit Berechnung

```python
# Property mit Berechnung
class Rechteck:
    def __init__(self, laenge, breite):
        self._laenge = laenge
        self._breite = breite

    @property
    def flaeche(self):
        return self._laenge * self._breite

# Objekt erstellen
rechteck1 = Rechteck(4, 6)

# Lesen der Property (wird die Fläche berechnen)
print("Fläche des Rechtecks:", rechteck1.flaeche)

```