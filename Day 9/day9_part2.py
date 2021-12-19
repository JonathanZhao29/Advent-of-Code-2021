#Jonathan Zhao's Code

#Read input
with open('Day 9\day9_input.txt') as file:
    contents = file.readlines()

#Adjust input and track bounds
height = len(contents)
width = len(contents[0])-2 #not counting \n
print(contents[0])
contents = ''.join(contents)
values = [char for char in contents] 

#Setup grid of values
grid = []
while '\n' in values: 
    grid.append(values[:values.index('\n')])
    values = values[values.index('\n')+1:]
grid.append(values)

#Stops recursive function from checking points it has checked before
pointsChecked = []

def CalcBasinValue(rowIndex, pointIndex,direction = 'none'):#Recursive function that returns the total basin value, optional direction value to not loop infinitely
    basinValue = 0
    #Does not continue if the value has been checked before
    if tuple([rowIndex,pointIndex]) not in pointsChecked:
        #Check if value is 9
        if grid[rowIndex][pointIndex] =='9':
            return 0
        else: #Add one to the basin value
            basinValue +=1
        pointsChecked.append(tuple([rowIndex,pointIndex])) #Add the point to the list of checked points
        #Check up if not edge 
        if rowIndex !=0 and direction !='down':
            basinValue += CalcBasinValue(rowIndex-1, pointIndex, 'up')
        #Check Right if not edge 
        if pointIndex != len(grid[rowIndex])-1 and direction !='left':
            basinValue += CalcBasinValue(rowIndex,pointIndex+1, 'right')

        #Check Down if not edge 
        if rowIndex !=len(grid)-1 and direction !='up':
            basinValue += CalcBasinValue(rowIndex+1, pointIndex, 'down')
        #Check Left if not edge 
        if pointIndex != 0 and direction !='right':
            basinValue += CalcBasinValue(rowIndex,pointIndex-1, 'left')
    return basinValue #Return the basin value


#Function to find basin
def lowPoints():
    basinValue = []
    for rowIndex in range(len(grid)):
        for pointIndex in range(len(grid[rowIndex])):
            if rowIndex ==0: #Top Row
                if pointIndex ==0:#Left Corner
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex]:#If lower than surroundings
                        basinValue.append(CalcBasinValue(rowIndex, pointIndex))
                elif pointIndex == width:#Right Corner  
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] <grid[rowIndex+1][pointIndex]:#If lower than surroundings
                        basinValue.append(CalcBasinValue(rowIndex, pointIndex))
                else:
                     #the rest of the top row
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex]:#If lower than surroundings
                        basinValue.append(CalcBasinValue(rowIndex, pointIndex))
            elif rowIndex ==len(grid)-1:#Bottom Row
                if pointIndex ==0:#Left Corner
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] <grid[rowIndex-1][pointIndex]:#If lower than surroundings
                        basinValue.append(CalcBasinValue(rowIndex, pointIndex))
                elif pointIndex == width: #Right Corner
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] <grid[rowIndex-1][pointIndex]:#If lower than surroundings
                        basinValue.append(CalcBasinValue(rowIndex, pointIndex))
                else:
                    if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1]and grid[rowIndex][pointIndex] <grid[rowIndex-1][pointIndex]:#If lower than surroundings
                        basinValue.append(CalcBasinValue(rowIndex, pointIndex))
            elif pointIndex == 0: #Left Column excluding corners
                if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex] and grid[rowIndex][pointIndex] < grid[rowIndex-1][pointIndex]:#If lower than surroundings
                    basinValue.append(CalcBasinValue(rowIndex, pointIndex))
            elif pointIndex == len(grid[rowIndex])-1:#Right Column excluding corners
                if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex] and grid[rowIndex][pointIndex] < grid[rowIndex-1][pointIndex]:#If lower than surroundings
                    basinValue.append(CalcBasinValue(rowIndex, pointIndex))
            else: #Every other case
                if grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex+1] and grid[rowIndex][pointIndex] < grid[rowIndex][pointIndex-1] and grid[rowIndex][pointIndex] < grid[rowIndex+1][pointIndex] and grid[rowIndex][pointIndex] < grid[rowIndex-1][pointIndex]:#If lower than surroundings
                    basinValue.append(CalcBasinValue(rowIndex, pointIndex))
    return basinValue


#Call Function to find risk values
basin = lowPoints()
#Sort the basins by descending order
basin.sort(reverse = True)
#Multiply the sizes
three_largest_basins = basin[0]*basin[1]*basin[2]

#Print Answer
print(three_largest_basins)