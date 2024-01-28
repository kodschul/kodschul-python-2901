# Python-Objekte Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Objekte-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Objekten in Python kennenlernen und wie sie in der objektorientierten Programmierung (OOP) verwendet werden. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Objekte erstellen

```python
# Objekte erstellen
class Hund:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

# Objekte der Klasse Hund erstellen
hund1 = Hund("Bello", 3)
hund2 = Hund("Luna", 5)

# Zugriff auf Attribute der Objekte
```

## Beispiel 2: Methoden in Objekten

```python
# Methoden in Objekten
class Rechteck:
    def __init__(self, laenge, breite):
        self.laenge = laenge
        self.breite = breite

    def berechne_flaeche(self):
        return self.laenge * self.breite

# Objekt der Klasse Rechteck erstellen
rechteck1 = Rechteck(4, 6)

# Aufruf der Methode des Objekts
flaeche = rechteck1.berechne_flaeche()
print("Fläche des Rechtecks:", flaeche)

```

## Beispiel 3: Objektvergleich

```python
# Objektvergleich
class Buch:
    def __init__(self, titel, autor):
        self.titel = titel
        self.autor = autor

# Objekte der Klasse Buch erstellen
buch1 = Buch("Python for Beginners", "John Doe")
buch2 = Buch("Python for Beginners", "John Doe")

# Objektvergleich
if buch1 == buch2:
    print("Die Bücher sind gleich.")
else:
    print("Die Bücher sind nicht gleich.")

```

## Beispiel 4: Verwendung von Objekten in Listen

```python
# Verwendung von Objekten in Listen
class Obst:
    def __init__(self, sort, farbe):
        self.sort = sort
        self.farbe = farbe

# Objekte der Klasse Obst erstellen und in einer Liste speichern
apfel = Obst("Apfel", "Rot")
banane = Obst("Banane", "Gelb")
orange = Obst("Orange", "Orange")

obst_liste = [apfel, banane, orange]

# Zugriff auf Objekte in der Liste
for obst in obst_liste:
    print(f"Sorte: {obst.sort}, Farbe: {obst.farbe}")

```