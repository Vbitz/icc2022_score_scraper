import pandas as pd
from json import loads
import matplotlib.pyplot as plt
import datetime

rows = []

with open("scores.json") as f:
	rows = [loads(line) for line in f]

for row in rows:
	row["time"] = datetime.datetime.strptime(row["time"].split(".")[0], "%Y-%m-%dT%H:%M:%S")

df = pd.DataFrame(rows).set_index("time")
# df.to_csv("scores.csv")
color_dict = {
	"United States of America": "#4169E1",
	"Asia": "#FFB6C1",
	"Oceania": "#8A2BE2",
	"Europe": "#FFD700",
	"Canada": "#DC143C",
	"Latin America": "#228B22",
	"Africa": "#FF8C00"
}
fig, axs = plt.subplots(figsize=(16, 6))
df.plot(ax=axs, color=[color_dict.get(x, '#333333') for x in df.columns], marker=".", grid=True)
# axs.set_yticks(range(0, 10000, 100), minor=True)
axs.set_xlim(
	pd.Timestamp(year=2022, month=6, day=16, hour=16),
	pd.Timestamp(year=2022, month=6, day=17, hour=1))
axs.legend(loc="upper left")
fig.savefig("scores.png")
