# Python-Dateibehandlung Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Dateibehandlung-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte der Dateibehandlung in Python kennenlernen, insbesondere das Lesen und Schreiben von Dateien unter Verwendung verschiedener Module wie JSON, pickle, shelve und HDF5 (h5py). Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Lesen und Schreiben von Textdateien

### Beispiel 1: Lesen einer Textdatei

```python
# Lesen einer Textdatei
with open("beispiel.txt", "r") as datei:
    inhalt = datei.read()
    print("Dateiinhalt:", inhalt)
```

## Beispiel 2: Schreiben in eine Textdatei

```python
# Schreiben in eine Textdatei
text_to_write = "Hallo, dies ist ein Beispieltext."

with open("neue_datei.txt", "w") as datei:
    datei.write(text_to_write)
```

## Beispiel 3: Lesen einer JSON-Datei

```python
import json

# Lesen einer JSON-Datei
with open("daten.json", "r") as datei:
    json_daten = json.load(datei)
    print("JSON-Daten:", json_daten)
```

## Beispiel 4: Schreiben in eine JSON-Datei

```python
# Schreiben in eine JSON-Datei
daten = {"name": "Max", "alter": 30, "stadt": "Berlin"}

with open("neue_daten.json", "w") as datei:
    json.dump(daten, datei)
```

## Beispiel 5: Lesen und Schreiben mit pickle

```python
import pickle

# Lesen und Schreiben mit pickle
daten = [1, 2, 3, 4, 5]

# Schreiben mit pickle
with open("daten.pickle", "wb") as datei:
    pickle.dump(daten, datei)

# Lesen mit pickle
with open("daten.pickle", "rb") as datei:
    geladene_daten = pickle.load(datei)
    print("Geladene Daten:", geladene_daten)
```

## Beispiel 6: Lesen und Schreiben mit shelve

```python
import shelve

# Lesen und Schreiben mit shelve
with shelve.open("datenbank") as db:
    db["name"] = "Anna"
    db["alter"] = 25

    geladener_name = db["name"]
    print("Geladener Name:", geladener_name)
```

## Beispiel 7: Lesen und Schreiben mit h5py

```python
import h5py

# Lesen und Schreiben mit h5py
daten = [1, 2, 3, 4, 5]

# Schreiben mit h5py
with h5py.File("daten.h5", "w") as datei:
    datei.create_dataset("dataset", data=daten)

# Lesen mit h5py
with h5py.File("daten.h5", "r") as datei:
    geladene_daten = list(datei["dataset"])
    print("Geladene Daten:", geladene_daten)
```