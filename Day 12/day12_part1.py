#Jonathan Zhao's Code

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

#Cave class to find all possi
class caves():
    def __init__(self, paths): #Setting up local variables, keeping track of all working paths and the cave connections
        self.paths = paths
        self.pathings = []
        self.end = 'end'
        self.start = 'start'
    
    def findPaths(self, currentLoc, currentPath, littles): #Finds all working paths
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
            for possiblePath in self.paths[currentLoc]: #For each possible path from current location
                if possiblePath not in littles: # If cave is not a little cave previously visited
                    self.findPaths(possiblePath, currentPath, littles)
        currentPath.pop() #Remove the current location
        if currentLoc in littles: #Removes the current location from the littles array
            littles.remove(currentLoc)
    
    def calcPaths(self): #Calls findPath and prints answer
        littles = []
        currentPath = []
        self.findPaths(self.start, currentPath, littles)
        print(len(self.pathings))



#Print Answer
cave_system = caves(paths)
cave_system.calcPaths()
