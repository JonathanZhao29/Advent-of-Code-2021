#Jonathan Zhao's Code

import numpy as np

#Read input
with open('Day 7\day7_input.txt') as file:
    contents = file.readlines()
    contents = ''.join(contents)
#Format input
crabs = [] #Horizontal position of all the crabs
while contents.find(',') !=-1:
    crabs.append(int(contents[:contents.find(',')]))
    contents = contents[contents.find(',')+1:]
crabs.append(int(contents)) #Final value in input

def calcFuel(position):#Calculates the increasing fuel cost per unit of distance
    fuelNeeded = 0
    for unit in range(1,position+1):
        fuelNeeded += unit
    return fuelNeeded

crabCount = np.bincount(crabs) #Amount of crabs at each horizontal position
#print(crabCount)

#First index
calcDistance = []
for crab in range(len(crabCount)):
    fuelCost =calcFuel(abs(0 - crab))
    calcDistance.append(fuelCost*crabCount[crab])
lowestdistance = sum(calcDistance) #Distance from a certain position to all other positions multiplied by the amount of crabs at the other positions

#The distances are in the shape of a parabola, with the lowest point being the most efficient
for index in range(1,len(crabCount)):
    calcDistance = []
    
    for crab in range(len(crabCount)): #Calculates the fuel cost from every other crab position
        fuelCost =calcFuel(abs(index - crab))
        calcDistance.append(fuelCost*crabCount[crab])
    if sum(calcDistance) < lowestdistance:#If it is more efficient, on left side of parabola
        lowestdistance = sum(calcDistance) #Track the most efficient
    else:#Stops from calculating the right half of the parabola
        break

#Print answer

print('Fuel spent for best position:',lowestdistance)