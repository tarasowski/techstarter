import os
import socket
import requests
import platform
import psutil

def test_file_exists():
    assert os.path.exists("example.txt"), "Die Datei 'example.txt' existiert nicht."

def test_service_availability():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        assert s.connect_ex(("example.com", 80)) == 0, "Der Dienst ist nicht verfügbar."

def test_file_size():
    file_size = os.path.getsize("example.txt")
    assert 100 <= file_size <= 1024, "Die Dateigröße ist außerhalb des erwarteten Bereichs."

def test_url_availability():
    response = requests.get("https://example.com")
    assert response.status_code == 200, "Die Webseite ist nicht verfügbar."

def test_config_file():
    with open("config.ini") as f:
        content = f.read()
        assert "debug = true" in content, "Die Debug-Einstellung fehlt in der Konfigurationsdatei."

def test_environment_variables():
    assert "API_KEY" in os.environ, "Die Umgebungsvariable 'API_KEY' fehlt."

def test_directory_exists():
    assert os.path.exists("/path/to/directory"), "Der Ordner existiert nicht."

def test_dns_resolution():
    assert socket.gethostbyname("example.com"), "Die DNS-Auflösung für 'example.com' ist fehlgeschlagen."

def test_process_running():
    assert "my_process" in (p.name() for p in psutil.process_iter()), "Der Prozess 'my_process' läuft nicht."

def test_system_architecture():
    assert platform.architecture()[0] == "64bit", "Das System ist keine 64-Bit-Architektur."
