import matplotlib.pyplot as plt
import pandas as pd

f = pd.read_csv("Mp-manager-data.csv", header=None, sep=";")

# name columns in Dataframe
f.columns = ["ID",
             "type",
             "code",
             "superior",
             "event",
             "category",
             "place",
             "date",
             "car_type",
             "street",
             "house_no",
             "lat",
             "lon"]

# get column with events (driving offences)
events = f["event"].value_counts()

# delete repeating part of sentence
events = events.rename(lambda x: x.replace("Přestupky podle zákona o silničním provozu - ", ""))

# sum less than top 10 counts into one slice
temp = events.head(10)
temp["others"] = sum(events[10:])

# plot pie chart
temp.plot.pie()
plt.show()
