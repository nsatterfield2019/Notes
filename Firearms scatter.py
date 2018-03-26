import csv
import matplotlib.pyplot as plt

with open("/Users/Nathan/PycharmProjects/Notes/FirearmsData.tsv") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)