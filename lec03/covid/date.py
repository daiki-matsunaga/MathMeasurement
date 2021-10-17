import json
import matplotlib.pyplot as plt
import numpy as np
import requests
import datetime as dt
import matplotlib.dates as mdates

data = requests.get("https://covid.ourworldindata.org/data/owid-covid-data.json").json()
#f = open('owid-covid-data.json', 'r')
#data = json.load(f)

country_data = data["JPN"]["data"]

print("Key list:")
for key in country_data[-1]:
    print(key)

dates = []
value = []
key = "new_cases"

# get data for each date
for datedata in country_data:
    t = datedata.get(key, "nan") # set value to nan if there is no data

    value.append(float(t)) # add to the list
    dates.append(datedata.get("date"))

dates = [dt.datetime.strptime(d, '%Y-%m-%d').date() for d in dates]

fig, ax = plt.subplots()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=120))

ax.plot(dates, value, 'o')
plt.gcf().autofmt_xdate()
ax.set_ylabel(key)
plt.show()
