#Jonathan Zhao's Code

#Read input
with open('Day 12\day12_input.txt') as file:
    contents = file.readlines()

#Format input into tuple pairs
connections = [line.strip() for line in contents] 
connections = [tuple([line[:line.find('-')],line[line.find('-')+1:]]) for line in connections]

#Put pairs into a dictionary, and removes 'start' from being a connection from another cave
paths = {}
for connection in connections:
        #Connects first cave to second cave
        if connection[1] !='start':
            if connection[0] not in paths : 
                paths[connection[0]] = [connection[1]]
            else:
                paths[connection[0]].append(connection[1])
        #Connects second cave to first cave
        if connection[0] != 'start':
            if connection[1] not in paths:
                paths[connection[1]] = [connection[0]]
            else:
                paths[connection[1]].append(connection[0])


#Cave class to find all possible working paths
class caves():
    def __init__(self, paths): #Setting up local variables, keeping track of all working paths and the cave connections
        self.paths = paths
        self.pathings = []
        self.end = 'end'
        self.start = 'start'
    
    def checkRepeats(self, littles): #Checks if list has duplicates
        for item in littles:
            if littles.count(item) > 1:
                return item
        return False

    def findPaths(self, currentLoc, currentPath, littles, repeated =''): #Finds all working paths
        #Record current location on path
        currentPath.append(currentLoc)
        #Add to littles if already visited small cave
        if currentLoc == currentLoc.lower():
            littles.append(currentLoc)
        #If we are at the end, record the path
        if currentLoc ==self.end:
            finalPath = currentPath[:]
            self.pathings.append(finalPath)
            currentPath.pop() #Remove the current location
            if currentLoc in littles: #Removes the current location from the littles array
                littles.remove(currentLoc)
        else:#If not at the end
            for possiblePath in self.paths[currentLoc]:
                if possiblePath not in littles:# If cave is not a little cave previously visited
                    self.findPaths(possiblePath, currentPath, littles,repeated)
                elif possiblePath == possiblePath.lower() and repeated =='':
                    self.findPaths(possiblePath, currentPath, littles,possiblePath)#Set repeated to possiblePath and run
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
