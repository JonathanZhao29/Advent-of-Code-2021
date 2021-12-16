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


crabCount = np.bincount(crabs) #Amount of crabs at each horizontal position
#print(crabCount)
distance = [] #Distance from a certain position to all other positions multiplied by the amount of crabs at the other positions
for index in range(len(crabCount)):
    calcDistance = [abs(index - crab)*crabCount[crab] for crab in range(len(crabCount))]
    distance.append(sum(calcDistance)) #Add that total distance to the array of distances

#Print answer
distance.sort() #Sort distances in ascending order
answer = distance[0] #Shortest distance
print('Fuel spent for best position:',answer)