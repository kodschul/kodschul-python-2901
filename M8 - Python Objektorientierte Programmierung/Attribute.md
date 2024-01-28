# Python-Attribute Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Attribute-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Attributen in Python kennenlernen, wie sie in Klassen und Objekten verwendet werden. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Klassenattribute

```python
# Klassenattribute
class Auto:
    anzahl_autos = 0  # Klassenattribut

    def __init__(self, marke):
        self.marke = marke
        Auto.anzahl_autos += 1

auto1 = Auto("Toyota")
auto2 = Auto("BMW")

print("Anzahl Autos:", Auto.anzahl_autos)  # Zugriff auf das Klassenattribut
```

## Beispiel 2: Instanzattribute

```python
# Instanzattribute
class Hund:
    def __init__(self, name, alter):
        self.name = name  # Instanzattribut
        self.alter = alter  # Instanzattribut

hund1 = Hund("Bello", 3)
hund2 = Hund("Luna", 5)

print(f"{hund1.name} ist {hund1.alter} Jahre alt.")
print(f"{hund2.name} ist {hund2.alter} Jahre alt.")
```

## Beispiel 3: Eigenschaften (Properties)

```python
# Eigenschaften (Properties)
class Kreis:
    def __init__(self, radius):
        self._radius = radius  # Privates Attribut

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            print("Der Radius kann nicht negativ sein.")
        else:
            self._radius = value

kreis1 = Kreis(5)
print("Aktueller Radius:", kreis1.radius)

kreis1.radius = 8
print("Neuer Radius:", kreis1.radius)

kreis1.radius = -3  # Hier wird die Setter-Methode aufgerufen und die Fehlermeldung ausgegeben.

```

## Beispiel 4: Dynamische Attribute

```python
# Dynamische Attribute
class Person:
    pass

person1 = Person()
person1.name = "Max"  # Dynamisch hinzugefügtes Attribut
person1.alter = 25

print(f"{person1.name} ist {person1.alter} Jahre alt.")

```