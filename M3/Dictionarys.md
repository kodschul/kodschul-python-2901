# Python-Dictionaries Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Dictionary-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Dictionaries in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Erstellung und Zugriff auf ein Dictionary

```python
# Erstellung und Zugriff auf ein Dictionary
student = {
    "name": "Max",
    "alter": 25,
    "note": 90
}

print("Name:", student["name"])
print("Alter:", student["alter"])
print("Note:", student["note"])
```

## Beispiel 2: Dictionary-Operationen

```python
# Dictionary-Operationen
student["note"] = 95  # Aktualisierung des Wertes für den Schlüssel "note"
student["fach"] = "Mathematik"  # Hinzufügen eines neuen Schlüssel-Wert-Paares

print("Aktualisierte Note:", student["note"])
print("Neues Fach:", student["fach"])
```

## Beispiel 3: Schleifen durch ein Dictionary

```python
# Schleifen durch ein Dictionary
for key, value in student.items():
    print(f"{key}: {value}")
```

## Beispiel 4: Überprüfen, ob ein Schlüssel vorhanden ist

```python
# Überprüfen, ob ein Schlüssel vorhanden ist
if "alter" in student:
    print("Der Schlüssel 'alter' ist im Dictionary vorhanden.")
else:
    print("Der Schlüssel 'alter' ist nicht im Dictionary vorhanden.")
```