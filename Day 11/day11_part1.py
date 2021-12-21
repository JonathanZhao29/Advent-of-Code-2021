#Jonathan Zhao's Code

#Read input
from os import pipe


with open('Day 11\day11_input.txt') as file:
    contents = file.readlines()

#Adjust input and track bounds
height = len(contents)
width = len(contents[0])-2 #not counting \n
contents = ''.join(contents)
values = [int(char) for char in contents if char != '\n'] 

#Setup grid of values
grid = []
while len(values) >0: 
    grid.append(values[:width+1])
    values = values[width+1:]


print(height,width)
print(grid)

#Simulate 100 steps, count total flashes


def checkIndex(rowIndex, pointIndex,flashed):
    if tuple([rowIndex,pointIndex]) not in flashed:#If not flashed yet
                grid[rowIndex][pointIndex] +=1 #Add one to the energy level for the energy from a nearby flash
                if grid[rowIndex][pointIndex] >=10: #If the energy level is above 9, meaning that it will flash
                    grid[rowIndex][pointIndex] = 0 #Set energy level to zero
                    flashed.append(tuple([rowIndex,pointIndex])) #Add that octopus to the list of flashed octopi
                    flash(rowIndex,pointIndex,flashed) #Initiate the flash

#Function for octopi flashing
def flash(rowIndex, pointIndex,flashed): #Based on the octopus's location, flash accordingly
    if rowIndex ==0: #Top Row
        if pointIndex ==0:#Left Corner
            checkIndex(rowIndex,pointIndex+1,flashed)
            checkIndex(rowIndex+1,pointIndex,flashed)
            checkIndex(rowIndex+1,pointIndex+1,flashed)
        elif pointIndex == width:#Right Corner  
            checkIndex(rowIndex,pointIndex-1,flashed)
            checkIndex(rowIndex+1,pointIndex,flashed)
            checkIndex(rowIndex+1,pointIndex-1,flashed)
        else:#the rest of the top row
            checkIndex(rowIndex,pointIndex+1,flashed)
            checkIndex(rowIndex,pointIndex-1,flashed)
            checkIndex(rowIndex+1,pointIndex,flashed)
            checkIndex(rowIndex+1,pointIndex+1,flashed)
            checkIndex(rowIndex+1,pointIndex-1,flashed)

    elif rowIndex ==len(grid)-1:#Bottom Row
        if pointIndex ==0:#Left Corner
            checkIndex(rowIndex,pointIndex+1,flashed)
            checkIndex(rowIndex-1,pointIndex,flashed)
            checkIndex(rowIndex-1,pointIndex+1,flashed)
        elif pointIndex == width: #Right Corner
            checkIndex(rowIndex,pointIndex-1,flashed)
            checkIndex(rowIndex-1,pointIndex,flashed)
            checkIndex(rowIndex-1,pointIndex-1,flashed)
        else:
            checkIndex(rowIndex,pointIndex+1,flashed)
            checkIndex(rowIndex,pointIndex-1,flashed)
            checkIndex(rowIndex-1,pointIndex,flashed)
            checkIndex(rowIndex-1,pointIndex+1,flashed)
            checkIndex(rowIndex-1,pointIndex-1,flashed)

    elif pointIndex == 0: #Left Column excluding corners
        checkIndex(rowIndex,pointIndex+1,flashed)
        checkIndex(rowIndex-1,pointIndex,flashed)
        checkIndex(rowIndex-1,pointIndex+1,flashed)
        checkIndex(rowIndex+1,pointIndex,flashed)
        checkIndex(rowIndex+1,pointIndex+1,flashed)

           
    elif pointIndex == len(grid[rowIndex])-1:#Right Column excluding corners
        checkIndex(rowIndex,pointIndex-1,flashed)
        checkIndex(rowIndex-1,pointIndex,flashed)
        checkIndex(rowIndex-1,pointIndex-1,flashed)
        checkIndex(rowIndex+1,pointIndex,flashed)
        checkIndex(rowIndex+1,pointIndex-1,flashed)
    else: #Every other case
        checkIndex(rowIndex,pointIndex+1,flashed)
        checkIndex(rowIndex,pointIndex-1,flashed)
        checkIndex(rowIndex-1,pointIndex,flashed)
        checkIndex(rowIndex-1,pointIndex+1,flashed)
        checkIndex(rowIndex-1,pointIndex-1,flashed)
        checkIndex(rowIndex+1,pointIndex,flashed)
        checkIndex(rowIndex+1,pointIndex+1,flashed)
        checkIndex(rowIndex+1,pointIndex-1,flashed)

flashCount = 0 #Amount of flashes
for step in range(100): #100 steps
    flashed = []#Track flashes in each step, an octopus can atmost flash once per step
    for row in range(len(grid)):
        grid[row] = [value+1 for value in grid[row]] #Add one to each energy level for the step

    for rowIndex in range(len(grid)):
        for pointIndex in range(len(grid[rowIndex])):
            if grid[rowIndex][pointIndex] not in flashed and grid[rowIndex][pointIndex] >=10 :#If at energy level 10 and not flashed yet
                    grid[rowIndex][pointIndex] = 0
                    flashed.append(tuple([rowIndex,pointIndex]))
                    flash(rowIndex, pointIndex,flashed)
    #Increase flash count by the amount of flashes that octopus causes
    flashCount +=len(flashed)
#Print Answer
print('Total flashes:',flashCount)