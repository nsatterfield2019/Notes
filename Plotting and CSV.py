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

# Make a line graph of comp users at three libraries by month

print(data)
month_names = data[0][1:-1]
print(month_names)

month_numbers = [x for x in range(12)]
print(month_numbers)

library_names = [x[0] for x in data]
print(library_names)

bwp_data =  data[library_names.index('Bucktown-Wicker Park')]
bwp_data.pop(0)
bwp_data.pop()
bwp_data = [int(x) for x in bwp_data]
print(bwp_data)



lp_data =  data[library_names.index('Lincoln Park')]
lp_data.pop(0)
lp_data.pop()
lp_data = [int(x) for x in lp_data]
print(lp_data)



hp_data =  data[library_names.index('Humboldt Park')]
hp_data.pop(0)
hp_data.pop()
hp_data = [int(x) for x in hp_data]
print(hp_data)


plt.figure(2, tight_layout=True)

plt.plot(month_numbers, bwp_data, label="Bucktown-Wicker Park")
plt.plot(month_numbers, hp_data, label='Humboldt Park')
plt.plot(month_numbers, lp_data, label='Lincoln Park')
plt.xticks(month_numbers, month_names, rotation=45)

plt.legend(bbox_to_anchor=(0, 1), loc="upper left")

plt.show()


