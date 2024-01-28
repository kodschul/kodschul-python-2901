# Python Installation

## Einführung

In diesem Abschnitt erfahren Sie, wie Sie Python auf Ihrem System installieren können. Folgen Sie den Schritten unten, um sicherzustellen, dass Sie Python erfolgreich einrichten.

## Schritt 1: Python herunterladen

Besuchen Sie die offizielle [Python-Website](https://www.python.org/), und klicken Sie auf den Button "Downloads". Wählen Sie die neueste stabile Version von Python aus.

## Schritt 2: Installationsassistent ausführen

Führen Sie die heruntergeladene Datei aus, um den Installationsassistenten zu starten. Stellen Sie sicher, dass Sie die Option "Add Python x.x to PATH" während der Installation aktivieren, um Python zum System-Pfad hinzuzufügen.

## Schritt 3: Installation überprüfen

Öffnen Sie die Kommandozeile (CMD) oder das Terminal und geben Sie die folgenden Befehle ein:

```bash
python --version
```

Dies sollte die installierte Python-Version anzeigen. Zusätzlich können Sie den folgenden Befehl verwenden, um die interaktive Python-Umgebung zu öffnen:

```bash
python
```

## Schritt 4: Pip (Paketmanager) installieren
Pip ist der Paketmanager für Python. Überprüfen Sie, ob Pip installiert ist, indem Sie den folgenden Befehl eingeben:

```bash
pip --version
```

Wenn Pip nicht installiert ist, können Sie es mit dem folgenden Befehl nachinstallieren:

```bash
python -m ensurepip --default-pip
```

## Schritt 5: Virtuelle Umgebung erstellen (optional)
Es wird empfohlen, virtuelle Umgebungen zu verwenden, um Projektabhängigkeiten zu isolieren. Erstellen Sie eine virtuelle Umgebung mit dem Befehl:

```bash
python -m venv myenv
```

Aktivieren Sie die virtuelle Umgebung:

Unter Windows: myenv\Scripts\activate
Unter Unix oder MacOS: source myenv/bin/activate