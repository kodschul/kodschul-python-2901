# Python-Bedingte Anweisungen Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-bedingte Anweisungen-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von bedingten Anweisungen in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Einfache if-Anweisung

```python
# Einfache if-Anweisung
alter = 18

if alter >= 18:
    print("Sie sind volljährig.")
```

## Beispiel 2: if-else-Anweisung

```python
# if-else-Anweisung
alter = 15

if alter >= 18:
    print("Sie sind volljährig.")
else:
    print("Sie sind minderjährig.")
```

## Beispiel 3: if-elif-else-Anweisung

```python
# if-elif-else-Anweisung
note = 75

if note >= 90:
    print("Sehr gut!")
elif note >= 70:
    print("Gut gemacht.")
else:
    print("Leistung verbessern.")
```

## Beispiel 4: Ternäre if-else-Anweisung

```python
# Ternäre if-else-Anweisung
ergebnis = "Bestanden" if note >= 50 else "Durchgefallen"
print("Prüfungsergebnis:", ergebnis)
```

## Beispiel 5: Verschachtelte if-Anweisungen

```python
# Verschachtelte if-Anweisungen
benutzername = "admin"
passwort = "geheim"

if benutzername == "admin":
    if passwort == "geheim":
        print("Anmeldung erfolgreich.")
    else:
        print("Falsches Passwort.")
else:
    print("Unbekannter Benutzer.")
```

## Beispiel 6: Verwendung von logischen Operatoren

```python
# Verwendung von logischen Operatoren
alter = 25

if alter >= 18 and alter <= 60:
    print("Sie sind im erwerbsfähigen Alter.")
else:
    print("Sie sind nicht im erwerbsfähigen Alter.")
```

## Beispiel 7: Überprüfung von Mitgliedschaft

```python
# Überprüfung von Mitgliedschaft
fruechte = ["Apfel", "Banane", "Orange"]
gesuchte_frucht = "Banane"

if gesuchte_frucht in fruechte:
    print("Die Frucht ist vorhanden.")
else:
    print("Die Frucht ist nicht vorhanden.")
```