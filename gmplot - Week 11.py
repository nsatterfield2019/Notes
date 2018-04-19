from gmplot import *
import csv

apikey = "AIzaSyD65be4pywe7-y4GjMmzZMidOpdmu2lkXo"

mymap = GoogleMapPlotter(41.923311, -87.638520, 14, apikey=apikey)

mymap.marker(41.923311, -87.638520) # lat, long

mymap.circle(41.933311, -87.638520, 500, "blue", ew=10) # lat, long, radius(m), color


lats = [41.923311 for x in range(10)]
longs = [-87.638520 - x/100 for x in range(10)]
lats[4] = 41.933311

mymap.plot(lats,longs, "red", ew=10) # lats, longs, color

mymap.polygon(lats, longs, fc="yellow", ec="black") # lats, longs, color, facecolor(fc), edgecolor(ec)

with open("/Users/Nathan/PycharmProjects/Notes/Parks_-_Public_Art.csv")


mymap.draw("mymap.html")



