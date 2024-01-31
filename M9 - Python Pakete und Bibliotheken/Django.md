# Python-Django Grundlagen Schulung für Anfänger

## Einführung

Herzlich willkommen zur Schulung für Python-Django-Grundlagen! In diesem Kurs werden wir die grundlegenden Konzepte von Django kennenlernen, einem leistungsstarken Webframework für die Entwicklung von Webanwendungen in Python. Hier sind einige Beispiele, um Ihnen einen guten Einstieg zu ermöglichen.

## Beispiel 1: Installation von Django

Bevor Sie Django verwenden können, müssen Sie es installieren. Sie können dies mit dem folgenden Befehl in Ihrer Python-Umgebung tun:

```python
pip install Django
```

## Beispiel 2: Erstellung eines Django-Projekts

```python
# Erstellung eines Django-Projekts
django-admin startproject meinprojekt
```

## Beispiel 3: Erstellung einer Django-Anwendung

```python
# Erstellung einer Django-Anwendung
cd meinprojekt
python manage.py startapp meineapp
```

## Beispiel 4: Definition von Modellen in Django

```python
# Definition von Modellen in Django
from django.db import models

class Artikel(models.Model):
    titel = models.CharField(max_length=200)
    inhalt = models.TextField()

    def __str__(self):
        return self.titel
```

## Beispiel 5: Ansichten und URLs in Django

```python
# Ansichten und URLs in Django
from django.urls import path
from . import views

urlpatterns = [
    path('', views.startseite, name='startseite'),
    path('artikel/<int:artikel_id>/', views.artikeldetail, name='artikeldetail'),
]
```