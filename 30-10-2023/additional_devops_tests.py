import os
import socket
import requests
import platform
import psutil
import subprocess

def test_file_not_exists():
    assert not os.path.exists("non_existent.txt"), "Die Datei 'non_existent.txt' existiert, sollte aber nicht existieren."

def test_service_unavailability():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        assert s.connect_ex(("example.com", 8080)) != 0, "Der Dienst sollte nicht verfügbar sein."

def test_file_size_range():
    file_size = os.path.getsize("example.txt")
    assert 500 <= file_size <= 2000, "Die Dateigröße ist außerhalb des erwarteten Bereichs."

def test_url_redirected():
    response = requests.get("http://www.example.com")
    assert response.history, "Die Webseite sollte umgeleitet werden."

def test_config_file_syntax():
    try:
        with open("invalid_config.ini") as f:
            content = f.read()
            assert "debug = true" in content, "Die Debug-Einstellung fehlt in der Konfigurationsdatei."
    except Exception as e:
        assert "Invalid config file" in str(e), "Die Konfigurationsdatei hat Syntaxfehler."

def test_environment_variable_absent():
    assert "SECRET_KEY" not in os.environ, "Die Umgebungsvariable 'SECRET_KEY' sollte nicht gesetzt sein."

def test_directory_absent():
    assert not os.path.exists("/non_existent_directory"), "Der Ordner 'non_existent_directory' existiert, sollte aber nicht existieren."

def test_dns_resolution_failure():
    try:
        socket.gethostbyname("non_existent_domain.com")
        assert False, "Die DNS-Auflösung sollte fehlschlagen."
    except socket.gaierror:
        pass

def test_process_not_running():
    assert "non_existent_process" not in (p.name() for p in psutil.process_iter()), "Der Prozess 'non_existent_process' sollte nicht laufen."

def test_system_architecture_32bit():
    assert platform.architecture()[0] == "32bit", "Das System sollte eine 32-Bit-Architektur haben."

def test_subprocess_execution():
    result = subprocess.check_output(["echo", "Hello, World!"]).decode().strip()
    assert result == "Hello, World!", "Das Subprozess-Ergebnis ist nicht wie erwartet."

def test_directory_write_permission():
    assert os.access("/tmp", os.W_OK), "Sie haben keine Schreibberechtigung im Verzeichnis '/tmp'."

def test_service_startup():
    try:
        subprocess.check_output(["systemctl", "start", "non_existent_service"])
        assert False, "Der Dienst 'non_existent_service' sollte nicht gestartet werden können."
    except subprocess.CalledProcessError:
        pass

def test_valid_ssl_certificate():
    response = requests.get("https://example.com")
    assert "CN=example.com" in response.text, "Das SSL-Zertifikat ist ungültig."

def test_tcp_port_open():
    assert socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect_ex(("example.com", 80)) == 0, "Der Port 80 auf 'example.com' sollte geöffnet sein."

def test_hostname_resolution():
    assert socket.gethostbyname("localhost") == "127.0.0.1", "Die Auflösung von 'localhost' ist nicht korrekt."

def test_firewall_rule_exists():
    assert "22" in subprocess.check_output(["iptables", "-L"]).decode(), "Die Firewall-Regel für Port 22 existiert nicht."

def test_network_interface_status():
    assert "UP" in subprocess.check_output(["ifconfig", "eth0"]).decode(), "Die Netzwerkschnittstelle 'eth0' sollte aktiviert sein."

def test_cpu_usage():
    assert psutil.cpu_percent(interval=1) >= 0, "Die CPU-Auslastung sollte positiv sein."

def test_memory_usage():
    assert psutil.virtual_memory().percent >= 0, "Der Speicherverbrauch sollte positiv sein."

