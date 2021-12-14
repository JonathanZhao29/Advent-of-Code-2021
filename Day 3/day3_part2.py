#Jonathan Zhao's Code
import numpy as np
#Read input file
with open('Day 3\day3_input.txt') as file:
    contents = file.readlines()
for value in np.arange(len(contents)): #Strips the extra space after each value
    contents[value] = contents[value].strip()


def greatestBit(values, index): #Func that returns 1 or 0 depending on which is more common
    ones = 0
    for value in values:
        if value[index] == '1':
            ones +=1
    if (len(values)- ones) >ones: #If there are more zeros than ones
        return '0'
    else:
        return '1'

def leastBit(values,index): #Func that returns 1 or 0 depending on which is less common
    ones = 0
    for value in values:
        if value[index] == '1':
            ones +=1
    #print(len(values), ones)
    if (len(values)- ones) >ones: #If there are more zeros than ones
        return '1'
    else:
        return '0'

#Oxygen rating
possibleO = contents
print(len(possibleO))
index = 0
while len(possibleO)>1:#While there are multiple possible answers
    gcb = greatestBit(possibleO, index)#Find the greatest common bit
    newPossibleO = []
    for value in possibleO: #Take all the values that are with that least common bit
        if  value[index] == gcb:
            newPossibleO.append(value)
    index +=1
    possibleO = newPossibleO #Change array to the values taken 
oxygen_rating = possibleO[0]


#CO2 scrubber rating
possibleC = contents
index = 0
while len(possibleC)>1: #While there are multiple possible answers
    lcb = leastBit(possibleC, index) #Find the least common bit
    newPossibleC = []
    for value in possibleC: #Take all the values that are with that least common bit
        if  value[index] == lcb:
            newPossibleC.append(value)

    index +=1
    possibleC = newPossibleC #Change array to the values taken 
co2_rate = possibleC[0]

#Calculating the final answer
output = int(oxygen_rating,2) *int(co2_rate,2)
print(int(oxygen_rating,2),int(co2_rate,2))
print(output)
