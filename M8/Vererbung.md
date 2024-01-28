# Python-Vererbung Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Vererbung-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Vererbung in Python kennenlernen und wie sie verwendet werden können, um Code wiederzuverwenden und die Struktur von Klassen zu organisieren. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Grundlegende Vererbung

```python
# Grundlegende Vererbung
class Tier:
    def __init__(self, name):
        self.name = name

    def lautgeben(self):
        print("Tier macht einen Laut")

class Hund(Tier):
    def lautgeben(self):
        print("Wuff!")

# Objekte erstellen
tier1 = Tier("Irgendein Tier")
hund1 = Hund("Bello")

# Methodenaufrufe
tier1.lautgeben()  # Gibt den generischen Tier-Laut aus
hund1.lautgeben()  # Gibt den spezifischen Hund-Laut aus
```

## Beispiel 2: Vererbung mit Super()

```python
# Vererbung mit Super()
class Fahrzeug:
    def __init__(self, marke, modell):
        self.marke = marke
        self.modell = modell

    def zeige_details(self):
        print(f"{self.marke} {self.modell}")

class Auto(Fahrzeug):
    def __init__(self, marke, modell, farbe):
        super().__init__(marke, modell)
        self.farbe = farbe

    def zeige_details(self):
        super().zeige_details()
        print(f"Farbe: {self.farbe}")

# Objekte erstellen
auto1 = Auto("Toyota", "Camry", "Blau")

# Methodenaufrufe
auto1.zeige_details()  # Gibt Details von Auto aus, inklusive der geerbten Methode von Fahrzeug

```

## Beispiel 3: Vererbung mit Mehrfachvererbung

```python
# Vererbung mit Mehrfachvererbung
class A:
    def methode(self):
        print("Methode von Klasse A")

class B(A):
    def methode(self):
        print("Methode von Klasse B")

class C(A):
    def methode(self):
        print("Methode von Klasse C")

class D(B, C):
    pass

# Objekt erstellen
objekt_d = D()

# Methodenaufruf (beim Aufruf wird die Methode von Klasse B verwendet)
objekt_d.methode()

```