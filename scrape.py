import requests
from datetime import datetime

API_URL = "https://www.ai-fitness.de/connect/v1/studio/1279902650/utilization"
DATEI = "werte.csv"

response = requests.get(API_URL, timeout=30)
response.raise_for_status()

data = response.json()

# Der tatsächliche Feldname im JSON
# Meist liefert die API z.B. {"utilizationPercent": 4}
wert = data.get("utilizationPercent")

if wert is None:
    raise ValueError(f"Ungültige API-Antwort: {data}")

zeit = datetime.now().isoformat()

with open(DATEI, "a", encoding="utf-8") as f:
    f.write(f"{zeit},{wert}\n")

print("Gespeichert:", zeit, wert)
