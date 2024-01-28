# Python-Boolean Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Boolean-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Booleans in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Booleans und Vergleichsoperatoren

```python
# Booleans und Vergleichsoperatoren
zahl1 = 10
zahl2 = 5

ist_groesser = zahl1 > zahl2
ist_gleich = zahl1 == zahl2

print("Ist zahl1 größer als zahl2?", ist_groesser)  # True
print("Ist zahl1 gleich zahl2?", ist_gleich)       # False
```

## Beispiel 2: Logische Operatoren

```python
# Logische Operatoren
ist_wahr = True
ist_falsch = False

und_operator = ist_wahr and ist_falsch
oder_operator = ist_wahr or ist_falsch
nicht_operator = not ist_wahr

print("Und-Operator:", und_operator)  # False
print("Oder-Operator:", oder_operator)  # True
print("Nicht-Operator:", nicht_operator)  # False
```

## Beispiel 3: Bedingungen mit Booleans

```python
# Bedingungen mit Booleans
hat_guthaben = True

if hat_guthaben:
    print("Kaufe ein neues Produkt.")
else:
    print("Lade dein Konto auf.")
```