#Jonathan Zhao's Code

#Read input
with open('Day 9\day9_input.txt') as file:
    contents = file.readlines()

#Adjust input and track bounds
height = len(contents)
width = len(contents[0])-2 #not counting \n
contents = ''.join(contents)
values = [char for char in contents] 

#Setup grid of values
grid = []
while '\n' in values: 
    grid.append(values[:values.index('\n')])
    values = values[values.index('\n')+1:]
grid.append(values)


#Function that finds if a point is a risk value based on its surrounding points, and checks for all edge cases
def lowPoints(grid):
    riskLevel = 0
    for rowIndex in range(len(grid)):
        for pointIndex in range(len(grid[rowIndex])):
            if rowIndex ==0: #Top Row
                if pointIndex ==0:#Left Corner
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex]:#If lower than surroundings
                        riskLevel += 1+int(grid[rowIndex][pointIndex])
                elif pointIndex == width:#Right Corner  
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] <grid[rowIndex+1][pointIndex]:#If lower than surroundings
                        riskLevel += 1+int(grid[rowIndex][pointIndex])
                else:
                     #the rest of the top row
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex]:#If lower than surroundings
                        riskLevel += 1+int(grid[rowIndex][pointIndex])
            elif rowIndex ==len(grid)-1:#Bottom Row
                if pointIndex ==0:#Left Corner
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] <grid[rowIndex-1][pointIndex]:#If lower than surroundings
                        riskLevel += 1+int(grid[rowIndex][pointIndex])
                elif pointIndex == width: #Right Corner
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] <grid[rowIndex-1][pointIndex]:#If lower than surroundings
                        riskLevel += 1+int(grid[rowIndex][pointIndex])
                else:
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1]and grid[rowIndex][pointIndex] <grid[rowIndex-1][pointIndex]:#If lower than surroundings
                        riskLevel += 1+int(grid[rowIndex][pointIndex])
            elif pointIndex == 0: #Left Column excluding corners
                if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex] and grid[rowIndex][pointIndex] < grid[rowIndex-1][pointIndex]:#If lower than surroundings
                    riskLevel += 1+int(grid[rowIndex][pointIndex])
            elif pointIndex == len(grid[rowIndex])-1:#Right Column excluding corners
                if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex] and grid[rowIndex][pointIndex] < grid[rowIndex-1][pointIndex]:#If lower than surroundings
                    riskLevel += 1+int(grid[rowIndex][pointIndex])
            else: #Every other case
                if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex] and grid[rowIndex][pointIndex] < grid[rowIndex-1][pointIndex]:#If lower than surroundings
                    riskLevel += 1+int(grid[rowIndex][pointIndex])
    return riskLevel

#Call Function to find risk values
riskLevel = lowPoints(grid)

#Print Answer
print(riskLevel)