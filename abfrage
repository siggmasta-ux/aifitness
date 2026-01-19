import requests
from datetime import datetime

API_URL = "https://www.ai-fitness.de/api/utilization?studio=duisburg-innenhafen"
DATEI = "werte.csv"

r = requests.get(API_URL, timeout=30)
r.raise_for_status()

data = r.json()

# robust: wir prüfen mehrere mögliche Feldnamen
wert = (
    data.get("occupiedPercent")
    or data.get("utilization")
    or data.get("occupancy")
)

if wert is None:
    raise ValueError(f"Kein Auslastungswert gefunden: {data}")

zeit = datetime.now().isoformat()

with open(DATEI, "a", encoding="utf-8") as f:
    f.write(f"{zeit},{wert}\n")

print("Gespeichert:", zeit, wert)
