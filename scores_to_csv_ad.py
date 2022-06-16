import pandas as pd
from json import loads
import matplotlib.pyplot as plt
import datetime

rows = []

with open("scores_ad.json") as f:
    rows = [loads(line) for line in f]

teams = {1: "Asia", 2: "United States of America", 3: "Canada",
         4: "Europe", 6: "Oceania", 7: "Latin America", 5: "Africa"}

summarized_rows = []
summarized_uptime = []

for row in rows:
    team_uptimes = {
        "time": datetime.datetime.strptime(row["time"].split(".")[0], "%Y-%m-%dT%H:%M:%S"),
        "United States of America": 0,
        "Asia": 0,
        "Oceania": 0,
        "Europe": 0,
        "Canada": 0,
        "Latin America": 0,
        "Africa": 0,
    }

    team_scores = {
        "time": datetime.datetime.strptime(row["time"].split(".")[0], "%Y-%m-%dT%H:%M:%S"),
        "United States of America": 0,
        "Asia": 0,
        "Oceania": 0,
        "Europe": 0,
        "Canada": 0,
        "Latin America": 0,
        "Africa": 0,
    }

    service_uptime = {}

    for score in row["aggregated_checks"]:
        service_uptime[str(score["teamId"]) + "-" + str(score["serviceId"])
                       ] = score["successfulChecks"] / score["totalChecks"]

    for score in row["team_services"]:
        if score["teamId"] in teams:
            uptime = service_uptime[str(
                score["teamId"]) + "-" + str(score["serviceId"])]

            if uptime > 0:
                team_scores[teams[score["teamId"]]
                            ] += (score["score"] * uptime)

            team_uptimes[teams[score["teamId"]]] += (uptime * 100) / 8

    summarized_rows += [team_scores]
    summarized_uptime += [team_uptimes]

df_scores = pd.DataFrame(summarized_rows).set_index("time")
df_uptime = pd.DataFrame(summarized_uptime).set_index("time")

df_scores.to_csv("scores.csv")
df_uptime.to_csv("uptime.csv")

color_dict = {
    "United States of America": "#4169E1",
    "Asia": "#FFB6C1",
    "Oceania": "#8A2BE2",
    "Europe": "#FFD700",
    "Canada": "#DC143C",
    "Latin America": "#228B22",
    "Africa": "#FF8C00"
}

fig, (axs1, axs2) = plt.subplots(1, 2, figsize=(24, 6))

df_scores.plot(ax=axs1, color=[color_dict.get(x, '#333333')
                               for x in df_scores.columns], grid=True)
axs1.set_xlim(
    pd.Timestamp(year=2022, month=6, day=16, hour=19),
    pd.Timestamp(year=2022, month=6, day=17, hour=1))
axs1.legend(loc="lower left")

df_uptime.plot(ax=axs2, color=[color_dict.get(x, '#333333')
                               for x in df_scores.columns], grid=True)
axs2.set_xlim(
    pd.Timestamp(year=2022, month=6, day=16, hour=19),
    pd.Timestamp(year=2022, month=6, day=17, hour=1))
axs2.legend(loc="lower left")

fig.savefig("scores.png")
