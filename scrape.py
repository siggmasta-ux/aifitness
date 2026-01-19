import requests
from datetime import datetime

API_URL = "https://www.ai-fitness.de/connect/v1/studio/1279902650/utilization"
DATEI = "werte.csv"

response = requests.get(API_URL, timeout=30)
response.raise_for_status()

data = response.json()

# aktuellen Zeitslot finden
current_items = [item for item in data["items"] if item.get("isCurrent")]

if not current_items:
    raise ValueError(f"Kein aktueller Zeitslot gefunden: {data}")

wert = current_items[0]["percentage"]

zeit = datetime.now().isoformat()

with open(DATEI, "a", encoding="utf-8") as f:
    f.write(f"{zeit},{wert}\n")

print("Gespeichert:", zeit, wert)
