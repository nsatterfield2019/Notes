import csv
import matplotlib.pyplot as plt
import numpy as np

with open("/Users/Nathan/PycharmProjects/Notes/FirearmsData.tsv") as f:
    reader = csv.reader(f, delimiter='\t')
    data = list(reader)

print(data)
headers = data.pop(0)
print(headers)

# plot homicides by firearm per 100K vs Firearms per 100

homicides_per100K = []
firearms_per100K = []
country_names = []

#no wars, no political unrest, established democracies
countries_to_plot = ["United States", "France", "Canada", "Germany", "England and Wales", "Ireland", "Sweden",
                     "Switzerland", "Norway", "Denmark", "Netherlands", "Spain", "Japan", "South Korea", "Australia",
                     "Russia", "China", "Israel"]

for i in range(len(data)):
    if data[i][0] in countries_to_plot:
        try:
            homicide = float(data[i][5])
            firearm = float(data[i][7])
            homicides_per100K.append(homicide)
            firearms_per100K.append(firearm)
            country_names.append(data[i][0])
        except:
            print(data[i][0], "has no data")

plt.figure(1, figsize=(12,7))
plt.scatter(firearms_per100K, homicides_per100K, s=20, c='red')
plt.title("World Homicide Rates vs Firearm Ownership")
plt.xlabel("Firearms per 100 people")
plt.ylabel("Homicides by Firearm per 100K population")

# make a best fit
m, b = np.polyfit(firearms_per100K, homicides_per100K, 1) # 1 for linear, returns slipe and y intercept

x = [0, 100]
y = [m * point + b for point in x]

plt.plot(x, y, color='green')

for i in range(len(country_names)):
    plt.annotate(country_names[i], xy=(firearms_per100K[i], homicides_per100K[i])) # text, xy=()

plt.show()
