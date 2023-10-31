import os
import socket
import requests
import platform
import psutil
import config # file name !!!
from config import API_KEY, OPENAI_KEY, change_api

print("this is my api key form config", API_KEY)
print("open ai api key", OPENAI_KEY)
change_api()

def test_file_exists():
    assert os.path.exists("config.py"), "Die Datei 'config.py' existiert nicht."

print("here is the first test")
test_file_exists()

def test_service_availability():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        assert s.connect_ex(("techstarter.de", 80)) == 0, "Der Dienst ist nicht verfügbar."

print("here is the second test")
test_service_availability()

def test_file_size():
    file_size = os.path.getsize("config.py")
    assert 30 <= file_size <= 1024, "Die Dateigröße ist außerhalb des erwarteten Bereichs."

print("here is the 3rd test")
test_file_size()

def test_url_availability():
    response = requests.get("https://google.com")
    assert response.status_code == 200, "Die Webseite ist nicht verfügbar."

print("test 4")
test_url_availability()

def test_config_file():
    with open("config.ini") as f:
        content = f.read()
        assert "debug = true" in content, "Die Debug-Einstellung fehlt in der Konfigurationsdatei."

def test_environment_variables():
    assert "API_KEY" in os.environ, "Die Umgebungsvariable 'API_KEY' fehlt."

test_environment_variables()

def test_directory_exists():
    assert os.path.exists("/path/to/directory"), "Der Ordner existiert nicht."

def test_dns_resolution():
    assert socket.gethostbyname("example.com"), "Die DNS-Auflösung für 'example.com' ist fehlgeschlagen."

def test_process_running():
    assert "my_process" in (p.name() for p in psutil.process_iter()), "Der Prozess 'my_process' läuft nicht."

def test_system_architecture():
    assert platform.architecture()[0] == "64bit", "Das System ist keine 64-Bit-Architektur."
