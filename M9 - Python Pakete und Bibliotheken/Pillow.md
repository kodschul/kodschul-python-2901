# Python-Pillow Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Pillow-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Pillow kennenlernen, einer Bibliothek für die Bildbearbeitung in Python. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Installation von Pillow

Bevor Sie Pillow verwenden können, müssen Sie es installieren. Sie können dies mit dem folgenden Befehl in Ihrer Python-Umgebung tun:

```python
pip install Pillow
```

## Beispiel 2: Öffnen und Anzeigen eines Bildes

```python
# Öffnen und Anzeigen eines Bildes
from PIL import Image

# Pfad zum Bild
bild_pfad = 'pfad/zum/bild.jpg'

# Bild öffnen
bild = Image.open(bild_pfad)

# Bild anzeigen
bild.show()
```

## Beispiel 3: Größenänderung eines Bildes

```python
# Größenänderung eines Bildes
neue_groesse = (300, 200)
neues_bild = bild.resize(neue_groesse)

# Neues Bild anzeigen
neues_bild.show()
```

## Beispiel 4: Drehen und Spiegeln eines Bildes

```python
# Drehen und Spiegeln eines Bildes
gedrehtes_bild = bild.rotate(90)
gespiegeltes_bild = bild.transpose(Image.FLIP_LEFT_RIGHT)

# Veränderte Bilder anzeigen
gedrehtes_bild.show()
gespiegeltes_bild.show()
```