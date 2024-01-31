# Python-TensorFlow Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-TensorFlow-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von TensorFlow kennenlernen, einer leistungsstarken Bibliothek für maschinelles Lernen und künstliche Intelligenz in Python. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Installation von TensorFlow

Bevor Sie TensorFlow verwenden können, müssen Sie es installieren. Sie können dies mit dem folgenden Befehl in Ihrer Python-Umgebung tun:

```python
pip install tensorflow
```

## Beispiel 2: Erstellung eines einfachen neuronalen Netzes

```python
# Erstellung eines einfachen neuronalen Netzes mit TensorFlow
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

# Modell erstellen
modell = Sequential([
    Dense(64, activation='relu', input_shape=(784,)),
    Dense(10, activation='softmax')
])

# Modellzusammenfassung anzeigen
modell.summary()
```

## Beispiel 3: Laden und Vorbereiten von Datensätzen

```python
# Laden und Vorbereiten von Datensätzen mit TensorFlow
from tensorflow.keras.datasets import mnist
from tensorflow.keras.utils import to_categorical

# Laden des MNIST-Datensatzes
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# Vorbereiten der Daten
x_train = x_train.reshape((60000, 28 * 28)).astype('float32') / 255
x_test = x_test.reshape((10000, 28 * 28)).astype('float32') / 255

y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
```

## Beispiel 4: Kompilieren und Trainieren des Modells

```python
# Kompilieren und Trainieren des Modells mit TensorFlow
modell.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Modell trainieren
modell.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_test, y_test))
```

## Beispiel 5: Vorhersagen mit dem trainierten Modell

```python
# Vorhersagen mit dem trainierten Modell
vorhersagen = modell.predict(x_test[:5])

# Anzeigen der Vorhersagen
print("Vorhersagen:")
print(vorhersagen)
```