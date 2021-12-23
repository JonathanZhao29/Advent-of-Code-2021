#Jonathan Zhao's Code

from collections import defaultdict
#Read input

with open('Day 12\day12_input.txt') as file:
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


class caves():
    def __init__(self, paths):
        self.paths = paths
        self.pathings = []
        self.end = 'end'
        self.start = 'start'
    
    def findPaths(self, currentLoc, currentPath, littles):
        #Record current location on path
        currentPath.append(currentLoc)
        #Add to littles if already visited small cave
        if currentLoc == currentLoc.lower():
            littles.append(currentLoc)
        #If we are at the end, record the path
        if currentLoc ==self.end:
            self.pathings.append(currentPath)
        else:
            #If not at the end
            for possiblePath in self.paths[currentLoc]:
                if possiblePath not in littles:
                    self.findPaths(possiblePath, currentPath, littles)
        currentPath.pop()
        if currentLoc in littles:
            littles.remove(currentLoc)
    
    def calcPaths(self):
        littles = []
        currentPath = []
        self.findPaths(self.start, currentPath, littles)
        print(len(self.pathings))



#Print Answer
cave_system = caves(paths)
cave_system.calcPaths()
