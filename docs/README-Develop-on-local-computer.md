

## Develop on local computer

#### Python creation of requirements.txt:
```bash
python3.10 -m venv ./venv
source venv/bin/activate
pip3.10 install pyttsx3==2.99
pip3.10 install PyPDF2==3.0.1
pip3.10 freeze > requirements.txt
deactivate
```

#### Python installation of requirements.txt:
```bash
python3.10 -m venv ./venv
source venv/bin/activate
python --version # Python 3.10.12
pip3.10 install -r requirements.txt
```

#### How to run in terminal:
```bash
python3.10 -m venv ./venv
source venv/bin/activate
python3.10 main.py
```
