import csv
import matplotlib.pyplot as plt

with open("/Users/Nathan/PycharmProjects/Notes/Libraries_computer_data.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)
# We want to plot computers users YTD vs library

names = [x[0] for x in data] # grabbing list of library names (alpabetical)
names = names[1:] # chop off header
print(names)

ytd = [x[-1] for x in data][1:]
ytd = [int(x) for x in ytd]
print(ytd)

library_number = [x for x in range(len(names))]
print(library_number)

# We want to plot computer users YTD vs library
plt.figure(1, figsize=(10, 7), tight_layout=True, facecolor='lightblue')
plt.bar(library_number, ytd, color='red')
plt.title("Chicago Library Branch Computer Usage - 2017")
plt.ylabel("Computer Users")


plt.xticks(library_number, names, rotation=90, fontsize=7) # plotted data, text to plot, rotation

plt.show()