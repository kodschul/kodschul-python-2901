# Python-Scikit-learn Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Scikit-learn-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Scikit-learn kennenlernen, einer Bibliothek für maschinelles Lernen in Python. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Installation von Scikit-learn

Bevor Sie Scikit-learn verwenden können, müssen Sie es installieren. Sie können dies mit dem folgenden Befehl in Ihrer Python-Umgebung tun:

```python
pip install scikit-learn
```

## Beispiel 2: Laden von Beispiel-Daten in Scikit-learn

```python
# Laden von Beispiel-Daten in Scikit-learn
from sklearn.datasets import load_iris

# Laden des Iris-Datensatzes
iris = load_iris()

# Ausgabe der Daten und Zielwerte
print("Daten:")
print(iris.data[:5])
print("\nZielwerte:")
print(iris.target[:5])
```

## Beispiel 3: Aufteilen von Daten in Trainings- und Testsets

```python
# Aufteilen von Daten in Trainings- und Testsets
from sklearn.model_selection import train_test_split

# Aufteilen der Daten und Zielwerte
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)

print("Anzahl Trainingsdaten:", len(X_train))
print("Anzahl Testdaten:", len(X_test))
```

## Beispiel 4: Trainieren eines einfachen Klassifikationsmodells

```python
# Trainieren eines einfachen Klassifikationsmodells
from sklearn.neighbors import KNeighborsClassifier

# Initialisierung des Klassifikators
knn = KNeighborsClassifier()

# Trainieren des Modells
knn.fit(X_train, y_train)

# Vorhersagen für Testdaten
vorhersagen = knn.predict(X_test)

print("Vorhersagen:")
print(vorhersagen)
```