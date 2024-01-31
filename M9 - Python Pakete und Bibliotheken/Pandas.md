# Python-Pandas Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Pandas-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Pandas kennenlernen, einer leistungsstarken Bibliothek für Datenanalyse und -manipulation. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Installation von Pandas

Bevor Sie Pandas verwenden können, müssen Sie es installieren. Sie können dies mit dem folgenden Befehl in Ihrer Python-Umgebung tun:

```python
pip install pandas
```

## Beispiel 2: Erstellung eines Pandas DataFrame

```python
# Erstellung eines Pandas DataFrame
import pandas as pd

daten = {'Name': ['Max', 'Anna', 'Tom'],
         'Alter': [25, 30, 22],
         'Stadt': ['Berlin', 'München', 'Hamburg']}

df = pd.DataFrame(daten)

print(df)
```

## Beispiel 3: Daten aus einem CSV-Datei einlesen

```python
# Daten aus einer CSV-Datei einlesen
pfad_zur_datei = 'pfad/zur/datei.csv'
df = pd.read_csv(pfad_zur_datei)

print(df.head())
```

## Beispiel 4: Grundlegende Datenmanipulation mit Pandas

```python
# Grundlegende Datenmanipulation mit Pandas
# Filtern nach Alter über 25
df_ober_25 = df[df['Alter'] > 25]

# Hinzufügen einer neuen Spalte
df['Beruf'] = ['Ingenieur', 'Lehrer', 'Student']

print("Daten über 25 Jahre:")
print(df_ober_25)
print("\nDataFrame nach Datenmanipulation:")
print(df)
```

## Beispiel 5: Aggregation und Gruppierung

```python
# Aggregation und Gruppierung
durchschnittsalter_pro_stadt = df.groupby('Stadt')['Alter'].mean()

print("Durchschnittsalter pro Stadt:")
print(durchschnittsalter_pro_stadt)
```