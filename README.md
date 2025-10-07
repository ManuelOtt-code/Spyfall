# Spyfall

Lokales Spyfall-Spiel mit E-Mail-Versand über die Gmail API.

## Voraussetzungen
- Python 3
- mamba oder conda
- Google-Konto
- pip

## Installation
git clone https://github.com/ManuelOtt-code/Spyfall
cd Spyfall
mamba env create -f environment.yml
mamba activate spyfall
# Alternativ:
conda env create -f environment.yml
conda activate spyfall

## Gmail API einrichten

1. Google Cloud Console öffnen und das richtige Projekt wählen.
2. Gmail API aktivieren.
3. OAuth-Zustimmungsbildschirm konfigurieren und den eigenen Account als Testnutzer eintragen.
4. OAuth-Client vom Typ Desktop erstellen und `credentials.json` ins Projektverzeichnis legen.
5. Erstanmeldung ausführen:
   ```bash
   python3 quickstart.py
# Spiel starten
python3 spyfall.py



