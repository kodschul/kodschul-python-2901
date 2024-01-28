# Python-Sets Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Sets-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Sets in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Erstellung und Zugriff auf ein Set

```python
# Erstellung und Zugriff auf ein Set
farben = {"Rot", "Blau", "Grün"}

# Elemente hinzufügen
farben.add("Gelb")

print("Alle Farben im Set:", farben)
```

## Beispiel 2: Set-Operationen

```python
# Set-Operationen
a = {1, 2, 3}
b = {3, 4, 5}

# Vereinigung von Sets
vereinigung = a.union(b)

# Schnittmenge von Sets
schnittmenge = a.intersection(b)

print("Vereinigung der Sets:", vereinigung)
print("Schnittmenge der Sets:", schnittmenge)
```

## Beispiel 3: Entfernen von Elementen

```python
# Entfernen von Elementen aus einem Set
farben.remove("Blau")

print("Set nach dem Entfernen:", farben)
```

## Beispiel 4: Überprüfung der Zugehörigkeit

```python
# Überprüfung der Zugehörigkeit zu einem Set
ist_rot_da = "Rot" in farben

print("Ist Rot im Set?", ist_rot_da)
```