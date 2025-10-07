# Spyfall

Local spyfall game where Emails are sent to detectives/spies by using the gmail api.

## Requirements
- Python 3
- mamba or conda
- Google account
- pip

# Installation
```bash
git clone https://github.com/ManuelOtt-code/Spyfall
cd Spyfall
mamba env create -f environment.yml
mamba activate spyfall
```
## Alternatively:
```bash
conda env create -f environment.yml
conda activate spyfall
```

# Setup of the Gmail API
1. Follow the instructions on https://developers.google.com/workspace/gmail/api/quickstart/python?hl=de 
2. Run quickstart.py
```bash
python3 quickstart.py
```
# Start the game
```bash
python3 spyfall.py
```



