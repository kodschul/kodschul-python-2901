# Python-Numpy Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Numpy-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Numpy kennenlernen, einer leistungsstarken Bibliothek für numerische Berechnungen in Python. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Installation von Numpy

Bevor Sie Numpy verwenden können, müssen Sie es installieren. Sie können dies mit dem folgenden Befehl in Ihrer Python-Umgebung tun:

```python
pip install numpy
```

## Beispiel 2: Erstellung von Numpy-Arrays

```python
# Erstellung von Numpy-Arrays
import numpy as np

# Erstellung eines einfachen Arrays
arr_einfach = np.array([1, 2, 3, 4, 5])

# Erstellung eines zweidimensionalen Arrays
arr_zweidimensional = np.array([[1, 2, 3], [4, 5, 6]])

print("Einfaches Numpy-Array:")
print(arr_einfach)
print("\nZweidimensionales Numpy-Array:")
print(arr_zweidimensional)
```

## Beispiel 3: Mathematische Operationen mit Numpy-Arrays

```python
# Mathematische Operationen mit Numpy-Arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Addition
ergebnis_addition = arr1 + arr2

# Multiplikation
ergebnis_multiplikation = arr1 * arr2

print("Ergebnis der Addition:")
print(ergebnis_addition)
print("\nErgebnis der Multiplikation:")
print(ergebnis_multiplikation)
```

## Beispiel 4: Indexierung und Slicing von Numpy-Arrays

```python
# Indexierung und Slicing von Numpy-Arrays
arr = np.array([10, 20, 30, 40, 50])

# Zugriff auf ein Element
element = arr[2]

# Slicing
teil_array = arr[1:4]

print("Zugriff auf ein Element:", element)
print("\nTeil-Array durch Slicing:")
print(teil_array)
```
