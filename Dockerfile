# Verwenden Sie ein offizielles Python-Image als Basis
FROM python:3.9-slim

# Setzen Sie das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopieren Sie die Anforderungen-Datei und installieren Sie die Abhängigkeiten
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopieren Sie den Rest der Anwendung
COPY . .

# Öffnen Sie den Port, auf dem die Flask-App läuft
EXPOSE 5000

# Befehl zum Ausführen der Anwendung
CMD ["python", "app.py"]
