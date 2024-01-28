# Python-Schleifen Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Schleifen-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Schleifen in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: while-Schleife

```python
# while-Schleife
zahl = 1

while zahl <= 5:
    print(zahl)
    zahl += 1
```

## Beispiel 2: for-Schleife mit Liste

```python
# for-Schleife mit Liste
fruechte = ["Apfel", "Banane", "Orange"]

for frucht in fruechte:
    print(frucht)
```

## Beispiel 3: for-Schleife mit range()

```python
# for-Schleife mit range()
for zahl in range(1, 6):
    print(zahl)
```

## Beispiel 4: break-Anweisung

```python
# break-Anweisung in einer Schleife
zahl = 1

while True:
    print(zahl)
    zahl += 1
    if zahl > 5:
        break
```

## Beispiel 5: continue-Anweisung

```python
# continue-Anweisung in einer Schleife
for zahl in range(1, 6):
    if zahl == 3:
        continue
    print(zahl)
```

## Beispiel 6: Schleifen mit else-Zweig

```python
# Schleifen mit else-Zweig
for zahl in range(1, 6):
    print(zahl)
else:
    print("Schleife beendet.")
```

## Beispiel 7: Nested Loops (verschachtelte Schleifen)

```python
# Verschachtelte Schleifen
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} * {j} = {i*j}")
```

## Beispiel 8: Schleifen mit Enumeration

```python
# Schleifen mit Enumeration
fruechte = ["Apfel", "Banane", "Orange"]

for index, frucht in enumerate(fruechte, start=1):
    print(f"{index}. {frucht}")
```