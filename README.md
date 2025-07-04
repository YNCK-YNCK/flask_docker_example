# flask_docker_example
Creates a docker container that runs a webserver with a flask API. This can be used to play around with requests module in python or to try cURL.

# Flask Docker Beispiel

Dieses Projekt zeigt, wie man eine einfache Flask-Anwendung in einem Docker-Container ausführt.

## Voraussetzungen

Bevor Sie beginnen, stellen Sie sicher, dass Sie Docker auf Ihrem System installiert haben. Sie können Docker von der offiziellen [Docker-Website](https://www.docker.com/get-started) herunterladen und installieren.

## Projektstruktur

- `app.py`: Die Flask-Anwendung.
- `Dockerfile`: Die Docker-Konfiguration zum Erstellen des Images.
- `requirements.txt`: Die Python-Paketabhängigkeiten.


## Anleitung

### 1. Repository klonen

Klonen Sie dieses Repository auf Ihren lokalen Computer:

```bash
git clone https://github.com/YNCK-YNCK/flask_docker_example.git
cd flask-docker-example

### 2. Docker-Image erstellen
Erstellen Sie das Docker-Image mit dem folgenden Befehl:

docker build -t flask-api .

### 3. Docker-Container starten
Starten Sie den Docker-Container mit dem folgenden Befehl:

docker run -p 5000:5000 flask-api


### 4. Anwendung testen

Öffnen Sie einen Webbrowser und navigieren Sie zu http://localhost:5000, um die Flask-Anwendung zu sehen. Für localhost:5000/api/settings ist neben GET auch POST möglich. Hier können Sie gerne ausprobieren, wie sie die Einstellungen über die API verändern können.

Beispiel cURL command:
curl -X POST -H "Content-Type: application/json" -d "{\"theme\":\"dark\",\"language\":\"de\"}" http://localhost:5000/api/settings

{"message":"Settings updated successfully","settings":{"language":"de","notifications":true,"theme":"dark"}}

Die Änderungen können dann direkt über cURL oder über den webbrowser abgerufen werden. Viel Spaß beim Ausprobieren! Vielleicht finden Sie ja noch ein kleines Geheimnis!

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Weitere Informationen finden Sie in der Datei LICENSE.
