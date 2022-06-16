import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime

resp = requests.get("https://icc-games.com/liveboard")

soup = BeautifulSoup(resp.text, "html.parser")

countries = soup.find_all("span", "liveboard-country")
scores = soup.find_all("span", "progress-number")

names = [t.text for t in countries]
scores_int = [float(t.text) for t in scores]

t = {a: b for a,b in zip(names, scores_int)}

t["time"] = datetime.now().isoformat()

print(json.dumps(t))
