import pandas as pd
import plotly.express as px
import csv
import math

with open("std_deviation.csv") as f:
    sf = csv.reader(f)
    fileData = list(sf)

data = fileData[0]
def mean(data):
    l = len(data)
    total = 0
    for x in data:
        total += int(x)
        
    mean = total/l
    return mean  

list_sq = []

for d in data:
    a = int(d)-mean(data)
    a = a**2
    list_sq.append(a)

sum = 0
for i in list_sq:
    sum += i

result = sum/ len(data)-1

sd = math.sqrt(result)

print("The result is ", sd)