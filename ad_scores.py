import requests
from json import loads, dumps
from datetime import datetime

team_services = requests.get("https://ad.icc-games.com/api/reports/public/6/teamServices.json")
aggregated_checks = requests.get("https://ad.icc-games.com/api/reports/public/6/aggregatedChecks.json")
checks = requests.get("https://ad.icc-games.com/api/reports/public/6/checks.json")

time = datetime.now().isoformat()

print(dumps({
	"time": time,
	"team_services": loads(team_services.text),
	"aggregated_checks": loads(aggregated_checks.text),
	"checks": loads(checks.text),
}))
