# Python-Wichtige Module in der Standardbibliothek

## Einführung

Die Python-Standardbibliothek bietet eine umfangreiche Sammlung von Modulen, die eine breite Palette von Funktionalitäten abdecken. In diesem Kurs werden wir einige wichtige Module in der Standardbibliothek kennenlernen, die häufig in der Entwicklung von Python-Anwendungen verwendet werden.

## 1. `os` - Betriebssystemfunktionalitäten

Das Modul `os` bietet Funktionen zum Interagieren mit dem Betriebssystem, wie z.B. Dateisystemoperationen, Umgebungsvariablen und Prozesssteuerung.

Beispiel:

```python
import os

# Aktuelles Arbeitsverzeichnis abrufen
aktuelles_verzeichnis = os.getcwd()
print("Aktuelles Verzeichnis:", aktuelles_verzeichnis)

# Dateien im Verzeichnis auflisten
dateien_im_verzeichnis = os.listdir()
print("Dateien im Verzeichnis:", dateien_im_verzeichnis)
```

## 2. datetime - Datum und Uhrzeit

```python
from datetime import datetime

# Aktuelles Datum und Uhrzeit abrufen
aktuelles_datum_und_uhrzeit = datetime.now()
print("Aktuelles Datum und Uhrzeit:", aktuelles_datum_und_uhrzeit)

# Formatierung des Datums
formatiertes_datum = aktuelles_datum_und_uhrzeit.strftime("%Y-%m-%d %H:%M:%S")
print("Formatiertes Datum:", formatiertes_datum)

```

## 3. random - Zufallszahlen

```python
import random

# Zufällige Ganzzahl zwischen 1 und 10 generieren
zufallszahl = random.randint(1, 10)
print("Zufallszahl:", zufallszahl)

# Zufälliges Element aus einer Liste auswählen
liste = ["Apfel", "Banane", "Orange", "Erdbeere"]
zufaelliges_element = random.choice(liste)
print("Zufälliges Element:", zufaelliges_element)

```

## 4. json - JSON-Verarbeitung

```python
import json

# JSON-Daten erstellen
daten = {"name": "Max", "alter": 30, "stadt": "Berlin"}
json_daten = json.dumps(daten)
print("JSON-Daten:", json_daten)

# JSON-Daten dekodieren
dekodierte_daten = json.loads(json_daten)
print("Dekodierte Daten:", dekodierte_daten)

```

## 5. requests - HTTP-Anfragen

```python
import requests

# HTTP GET-Anfrage senden
url = "https://api.example.com/data"
antwort = requests.get(url)

# Antwortinhalt anzeigen
print("Antwortinhalt:", antwort.text)


```