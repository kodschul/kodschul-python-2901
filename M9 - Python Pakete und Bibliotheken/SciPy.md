# Python-Scipy Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Scipy-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Scipy kennenlernen, einer Bibliothek für wissenschaftliche Berechnungen und Signalverarbeitung in Python. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Installation von Scipy

Bevor Sie Scipy verwenden können, müssen Sie es installieren. Sie können dies mit dem folgenden Befehl in Ihrer Python-Umgebung tun:

```python
pip install scipy
```

## Beispiel 2: Integration mit Scipy

```python
# Integration mit Scipy
from scipy import integrate
import numpy as np

# Funktion für die Integration
funktion = lambda x: x**2

# Durchführung der Integration
ergebnis, fehler = integrate.quad(funktion, 0, 1)

print("Ergebnis der Integration:", ergebnis)
print("Fehler der Integration:", fehler)
```

## Beispiel 3: Lösung von Differentialgleichungen mit Scipy

```python
# Lösung von Differentialgleichungen mit Scipy
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Differentialgleichung: y'(t) = -2y(t)
funktion = lambda t, y: -2 * y

# Anfangsbedingung
anfangsbedingung = [1]

# Lösung der Differentialgleichung
ergebnis = solve_ivp(funktion, [0, 5], anfangsbedingung, t_eval=np.linspace(0, 5, 100))

# Plot der Lösung
plt.plot(ergebnis.t, ergebnis.y[0])
plt.xlabel('Zeit')
plt.ylabel('y(t)')
plt.title('Lösung der Differentialgleichung')
plt.show()
```

## Beispiel 4: Anwendung von Filtern auf Signale mit Scipy

```python
# Anwendung von Filtern auf Signale mit Scipy
from scipy.signal import butter, lfilter
import numpy as np
import matplotlib.pyplot as plt

# Erzeugung eines Beispielsignals
t = np.linspace(0, 1, 1000, endpoint=False)
signal = np.sin(2 * np.pi * 5 * t) + 0.5 * np.sin(2 * np.pi * 20 * t)

# Entwurf eines Bandpass-Filters
untere_grenze = 4
obere_grenze = 10
ordnung = 4
b, a = butter(ordnung, [untere_grenze, obere_grenze], btype='band', fs=1000)

# Anwendung des Filters auf das Signal
gefiltertes_signal = lfilter(b, a, signal)

# Plot des Originalsignals und des gefilterten Signals
plt.plot(t, signal, label='Originalsignal')
plt.plot(t, gefiltertes_signal, label='Gefiltertes Signal')
plt.xlabel('Zeit')
plt.ylabel('Amplitude')
plt.title('Anwendung eines Bandpass-Filters auf ein Signal')
plt.legend()
plt.show()
```