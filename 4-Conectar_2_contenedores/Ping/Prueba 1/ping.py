import requests

def ping(host):
    try:
        response = requests.get(f"http://{host}:8000")
        response.raise_for_status()
        print(f"Successfully connected to {host}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to {host}: {e}")

ping('container2')
