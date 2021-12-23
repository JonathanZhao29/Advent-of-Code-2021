#Jonathan Zhao's Code

from collections import defaultdict
#Read input

with open('Day 12\day12_test_input.txt') as file:
    contents = file.readlines()

#Format input into tuple pairs
connections = [line.strip() for line in contents] 
connections = [tuple([line[:line.find('-')],line[line.find('-')+1:]]) for line in connections]
#Put pairs into a dictionary
paths = {}
for connection in connections:
    if connection[0] not in paths:
        paths[connection[0]] = [connection[1]]
    else:
        paths[connection[0]].append(connection[1])
    if connection[1] not in paths:
        paths[connection[1]] = [connection[0]]
    else:
        paths[connection[1]].append(connection[0])
print(paths)

pathings = [] #Tracks all paths
littles = ['start'] #Tracks little caves
def checkPaths(startLocation, endLocation,currentPath, littles):
    currentPath.append(startLocation)
    print(currentPath)
    if startLocation == endLocation:
        pathings.append(currentPath)
        littles.clear()
        littles.append('start')
        currentPath.clear()
        currentPath.append('start')
    else:
        for possiblePath in paths[startLocation]: #For each possible route from that cave
            if possiblePath not in littles: #If not a small cave that has already been visited
                if possiblePath == possiblePath.lower(): #If it is a small cave
                    littles.append(possiblePath)
                current = possiblePath
                checkPaths(current,endLocation, currentPath, littles)


checkPaths('start','end',[], littles)

#Print Answer
print('total paths', len(pathings))
