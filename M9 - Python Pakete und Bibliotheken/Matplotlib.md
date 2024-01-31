# Python-Matplotlib Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Matplotlib-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Matplotlib kennenlernen, einer Bibliothek zur Erstellung von Diagrammen und Visualisierungen in Python. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Installation von Matplotlib

Bevor Sie Matplotlib verwenden können, müssen Sie es installieren. Sie können dies mit dem folgenden Befehl in Ihrer Python-Umgebung tun:

```python
pip install matplotlib
```

## Beispiel 2: Einfaches Linien-Diagramm

```python
# Einfaches Linien-Diagramm mit Matplotlib
import matplotlib.pyplot as plt

# Daten für das Diagramm
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

# Erstellung des Linien-Diagramms
plt.plot(x, y)

# Beschriftungen hinzufügen
plt.title('Einfaches Linien-Diagramm')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')

# Diagramm anzeigen
plt.show()
```

## Beispiel 3: Balkendiagramm

```python
# Balkendiagramm mit Matplotlib
kategorien = ['A', 'B', 'C', 'D']
werte = [4, 7, 2, 5]

# Erstellung des Balkendiagramms
plt.bar(kategorien, werte, color='skyblue')

# Beschriftungen hinzufügen
plt.title('Balkendiagramm')
plt.xlabel('Kategorien')
plt.ylabel('Werte')

# Diagramm anzeigen
plt.show()
```

## Beispiel 4: Punktwolke

```python
# Punktwolke mit Matplotlib
import numpy as np

# Daten für die Punktwolke
x = np.random.rand(50)
y = np.random.rand(50)

# Erstellung der Punktwolke
plt.scatter(x, y, color='red')

# Beschriftungen hinzufügen
plt.title('Punktwolke')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')

# Diagramm anzeigen
plt.show()
```