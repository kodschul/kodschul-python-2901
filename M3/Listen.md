# Python-Listen Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Listen-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Listen in Python kennenlernen. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Erstellung und Zugriff auf eine Liste

```python
# Erstellung und Zugriff auf eine Liste
fruechte = ["Apfel", "Banane", "Orange"]

print("Erstes Element:", fruechte[0])
print("Letztes Element:", fruechte[-1])
```

## Beispiel 2: Listenoperationen

```python
# Listenoperationen
zahlen = [1, 2, 3]

# Hinzufügen eines Elements
zahlen.append(4)

# Entfernen eines Elements
zahlen.remove(2)

print("Aktuelle Liste:", zahlen)
```

## Beispiel 3: Listeniteration

```python
# Listeniteration
for frucht in fruechte:
    print(frucht)
```

## Beispiel 4: Listenslicing

```python
# Listenslicing
teil_der_liste = fruechte[1:3]

print("Teil der Liste:", teil_der_liste)
```