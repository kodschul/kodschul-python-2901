# Python-Klassen Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Klassen-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Klassen in Python kennenlernen, wie sie für die Objektorientierte Programmierung (OOP) verwendet werden. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Klassen erstellen

```python
# Klassen erstellen
class Auto:
    def __init__(self, marke, farbe):
        self.marke = marke
        self.farbe = farbe

    def zeige_details(self):
        print(f"Marke: {self.marke}, Farbe: {self.farbe}")

# Objekte erstellen
auto1 = Auto("Toyota", "Blau")
auto2 = Auto("BMW", "Rot")

# Methoden aufrufen
auto1.zeige_details()
auto2.zeige_details()
```

## Beispiel 2: Vererbung

```python
# Vererbung
class Elektroauto(Auto):
    def __init__(self, marke, farbe, batteriekapazitaet):
        super().__init__(marke, farbe)
        self.batteriekapazitaet = batteriekapazitaet

    def zeige_details(self):
        super().zeige_details()
        print(f"Batteriekapazität: {self.batteriekapazitaet} kWh")

# Objekte erstellen
elektroauto1 = Elektroauto("Tesla", "Silber", 75)
elektroauto2 = Elektroauto("Nissan", "Grün", 60)

# Methoden aufrufen
elektroauto1.zeige_details()
elektroauto2.zeige_details()
```

## Beispiel 3: Klassenattribute

```python
# Klassenattribute
class Mitarbeiter:
    anzahl_mitarbeiter = 0  # Klassenattribut

    def __init__(self, name):
        self.name = name
        Mitarbeiter.anzahl_mitarbeiter += 1

# Objekte erstellen
mitarbeiter1 = Mitarbeiter("Anna")
mitarbeiter2 = Mitarbeiter("Max")

print("Anzahl Mitarbeiter:", Mitarbeiter.anzahl_mitarbeiter)
```

## Beispiel 4: Statische Methoden

```python
# Statische Methoden
class Mathematik:
    @staticmethod
    def addiere(a, b):
        return a + b

# Verwendung der statischen Methode
ergebnis = Mathematik.addiere(3, 5)
print("Ergebnis der Addition:", ergebnis)
```