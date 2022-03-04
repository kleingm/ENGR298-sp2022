from file_utils import load_with_pickle
from covid_point import CovidRecord
import numpy as np

# load covid data as list of CovidRecord objects
data = load_with_pickle('covid_data.pickle')


# create new list of Rockingham County, VA data
rockinghamvalist = list()

for obj in data:
    if obj.county == 'Rockingham' and int(obj.cases)>0:
             rockinghamvalist.append(obj.date)
print('The first covid case reported in Rockingham county was ' + str(rockinghamvalist[0]))
# write code to address the following question:
# When was the first positive COVID case in Rockingham County and Harrisonburg?
harrisonburgvalist = list()
for obj in data:
    if obj.county == 'Harrisonburg city' and int(obj.cases)>0:
             harrisonburgvalist.append(obj.date)
print('The first covid case reported in Harrisonburg city  was ' + str(harrisonburgvalist[0]))
# 2020-03-22,Rockingham,Virginia,51165,2,0 should be the answer
# 2020-03-13,Harrisonburg city,Virginia,51660,1,0 is the answer for HBURG
# write code to address the following question:
# What day was the greatest number of new daily cases recorded in Harrisonburg and Rockingham County?
rockinghamcases = list()
for obj in data:
    if obj.county == 'Rockingham':
        rockinghamcases.append(int(obj.cases))
listdiffrhamcases = np.diff(rockinghamcases)
print("The greatest number of new daily covid cases in Rockingham county is " +str(max(listdiffrhamcases)))

hburgcases = list()
for obj in data:
    if obj.county == 'Harrisonburg city':
        hburgcases.append(int(obj.cases))
listdiffhburgcases = np.diff(hburgcases)
print("The greatest number of new daily cases in Harrisonburg is " +str(max(listdiffhburgcases)))

# write code to address the following question:
# In terms of absolute number of cases, when was the worst seven-day period in the city/county for new COVID cases?
# harrisonburg city 7 day period
max = 0
startIndexofMax = 0
for i in range(0,(len(listdiffhburgcases)-7)):
    tempmax = 0
    for j in range(0, 7):
       tempmax += listdiffhburgcases[i+j]
    if (tempmax > max):
        max = tempmax
        startIndexofMax = i

# harrisonburgvalist dates list
datesofMax = list()

for x in range(0,7):
    datesofMax.append(harrisonburgvalist[startIndexofMax +x])

print("In terms of absolute number of cases, the worst 7-day period of COVID for Harrisonburg city, VA was " + str(datesofMax))

max1 = 0
startIndexofMax1 = 0
for i in range(0,(len(listdiffrhamcases)-7)):
    tempmax = 0
    for j in range(0, 7):
       tempmax += listdiffrhamcases[i+j]
    if tempmax > max1:
        max1 = tempmax
        startIndexofMax1 = i

# rham dates list
datesofMax1 = list()

for x in range(0,7):
    datesofMax1.append(rockinghamvalist[startIndexofMax1 +x])

print("In terms of absolute number of cases, the worst 7-day period of COVID for Rockingham county, VA was " + str(datesofMax1))
# write code to address the following question:
# In terms of absolute number of cases, when was the rise in cases the fastest over a rolling week window?
# Over what period in cases  was the rise the greatest
slopehburg = (np.gradient(listdiffhburgcases))
max2 = 0
startIndexofMax2 = 0
for i in range(0,(len(slopehburg)-7)):
    tempmax = 0
    for j in range(0, 7):
       tempmax += slopehburg[i+j]
    if tempmax > max:
        max2 = tempmax
        startIndexofMax2 = i
datesofMax2 = list()

for x in range(0,7):
    datesofMax2.append(harrisonburgvalist[startIndexofMax2 +x])
print("The greatest rise in cases over a 7-day period in Harrisonburg city, VA was " +str(datesofMax2))

# greatest rise in cases for rockingham county
sloperham = (np.gradient(listdiffrhamcases))
max3 = 0
startIndexofMax3 = 0
for i in range(0,(len(sloperham)-7)):
    tempmax = 0
    for j in range(0, 7):
       tempmax += sloperham[i+j]
    if tempmax > max:
        max3 = tempmax
        startIndexofMax3 = i
datesofMax3 = list()

for x in range(0,7):
    datesofMax3.append(rockinghamvalist[startIndexofMax3 +x])
print("The greatest rise in cases over a 7-day period in Rockingham county, VA was " +str(datesofMax3))

