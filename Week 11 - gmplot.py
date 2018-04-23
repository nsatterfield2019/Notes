from gmplot import *
import csv

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"


mymap = GoogleMapPlotter(41.923311, -87.638520, 12, apikey=apikey)
'''
mymap.marker(41.923311, -87.638520) # lat, long

mymap.circle(41.933311, -87.638520, 500, "blue", ew=10) # lat, long, radius(m), color


lats = [41.923311 for x in range(10)]
longs = [-87.638520 - x/100 for x in range(10)]
lats[4] = 41.933311

mymap.plot(lats,longs, "red", ew=10) # lats, longs, color

mymap.polygon(lats, longs, fc="yellow", ec="black") # lats, longs, color, facecolor(fc), edgecolor(ec)
'''

with open("/Users/Nathan/PycharmProjects/Notes/Parks_-_Public_Art.csv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data.pop(0))


lats = [float(x[-3]) for x in data]
longs = [float(x[-2]) for x in data]

mymap.scatter(lats, longs, color="green", marker=True, size=1, opacity=1)

'''
for i in range(len(lats)):
    mymap.circle(lats[i], longs[i], i) # like scatter but we can vary color and zie
'''

mymap.heatmap(lats, longs, maxIntensity=5, radius=50, dissipating=True)

mymap.draw("mymap.html")



