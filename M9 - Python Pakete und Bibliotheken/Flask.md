# Python-Flask Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Flask-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Flask kennenlernen, einem Webframework für die Entwicklung von Webanwendungen in Python. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Installation von Flask

Bevor Sie Flask verwenden können, müssen Sie es installieren. Sie können dies mit dem folgenden Befehl in Ihrer Python-Umgebung tun:

```python
pip install Flask
```

## Beispiel 2: Einfache Flask-Anwendung

```python
# Einfache Flask-Anwendung
from flask import Flask

# Flask-App erstellen
app = Flask(__name__)

# Routen definieren
@app.route('/')
def startseite():
    return 'Willkommen auf der Startseite!'

# Flask-App ausführen
if __name__ == '__main__':
    app.run(debug=True)
```

## Beispiel 3: Dynamische Routen

```python
# Dynamische Routen in Flask
from flask import Flask

app = Flask(__name__)

# Dynamische Route
@app.route('/benutzer/<name>')
def benutzerseite(name):
    return 'Willkommen auf der Benutzerseite, {}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)
```

## Beispiel 4: HTML-Vorlagen in Flask

```python
# Verwendung von HTML-Vorlagen in Flask
from flask import Flask, render_template

app = Flask(__name__)

# Routen definieren
@app.route('/')
def startseite():
    return render_template('startseite.html', titel='Willkommen', text='Herzlich willkommen auf der Startseite!')

if __name__ == '__main__':
    app.run(debug=True)
```