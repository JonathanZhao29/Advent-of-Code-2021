#Jonathan Zhao's Code
# This code is adapted from Divyanshu Mehta, the original example code is here:
# https://www.geeksforgeeks.org/python-program-for-dijkstras-shortest-path-algorithm-greedy-algo-7/

import sys

#Read input
with open('Day 15\day15_input.txt') as file:
    contents = file.readlines()

#Strip empty space from end of each line
connections = [line.strip() for line in contents] 
#Size of the 2d array
size = len(connections)*len(connections[0])

class Graph():
 
    def __init__(self, vertices, riskGraph):
        self.V = vertices #Vertices on the graph
        self.riskGraph = riskGraph #2d array with risk values
        #Since input is a square, get the length of one side
        self.size = len(riskGraph)
 
    def totalRisk(self, dist): #Prints total risk
        print ('Path with lowest risk:',dist[-1])

 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search nearest vertex not in the
        # shortest path tree
        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u
 
        return min_index
 
    #Return the the location and risk value of surrounding nodes
    def surroundingNodes(self, minV):
        #Find row and column length
        row = minV//self.size
        col = minV%self.size
        edges = [] #Surrounding nodes

        #Figure out the surrounding nodes and risk levels of each node
        #Top Row
        if row ==0:
            #Left Column
            if col == 0:
                edges = [[row,col+1,int(self.riskGraph[row][col+1])],[row+1,col,int(self.riskGraph[row+1][col])]]
            #Right Column:
            elif col == self.size-1:
                edges = [[row,col-1,int(self.riskGraph[row][col-1])],[row+1,col,int(self.riskGraph[row+1][col])]]
            #else:
            else:
                edges = [[row,col+1,int(self.riskGraph[row][col+1])],[row,col-1,int(self.riskGraph[row][col-1])],[row+1,col,int(self.riskGraph[row+1][col])]]
        #Bottom Row
        elif row == self.size-1:
            #Left Column
            if col == 0:
                edges = [[row,col+1,int(self.riskGraph[row][col+1])],[row-1,col,int(self.riskGraph[row-1][col])]]
            #Right Column:
            elif col == self.size-1:
                edges = [[row,col-1,int(self.riskGraph[row][col-1])],[row-1,col,int(self.riskGraph[row-1][col])]]
            #else:
            else:
                edges = [[row,col+1,int(self.riskGraph[row][col+1])],[row,col-1,int(self.riskGraph[row][col-1])],[row-1,col,int(self.riskGraph[row-1][col])]]
        #Else
        else:
            #Left Column
            if col == 0:
                edges = [[row,col+1,int(self.riskGraph[row][col+1])],[row-1,col,int(self.riskGraph[row-1][col])],[row+1,col,int(self.riskGraph[row+1][col])]]
            #Right Column:
            elif col == self.size-1:
                edges = [[row,col-1,int(self.riskGraph[row][col-1])],[row-1,col,int(self.riskGraph[row-1][col])],[row+1,col,int(self.riskGraph[row+1][col])]]
            #else:
            else:
                edges = [[row,col+1,int(self.riskGraph[row][col+1])],[row,col-1,int(self.riskGraph[row][col-1])],[row-1,col,int(self.riskGraph[row-1][col])],[row+1,col,int(self.riskGraph[row+1][col])]]
        #Return these surrounding nodes
        return edges


    # Function that implements Dijkstra's shortest path algorithm
    def dijkstra(self, src): #src is starting position
        
        #Set every item in list to max integer size
        dist = [sys.maxsize] * self.V
        
        dist[src] = 0 #Starting Position
        sptSet = [False] * self.V #List of visited statuses, set to false 
 
        for count in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # minV is always equal to src in first iteration
            minV = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[minV] = True
 

            #Find then surrounding nodes
            surrounding = self.surroundingNodes(minV)
            
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # risk is greater than new risk and
            # the vertex in not in the shortest path tree
            for n in surrounding:
                #If not in visited list and risk is lower than current 
                #Here, n[0] is row, n[1] is column, and n[2] is risk
                if sptSet[n[0]*self.size+n[1]] ==False and dist[n[0]*self.size+n[1]]> dist[minV] + n[2]:
                    dist[n[0]*self.size+n[1]] = dist[minV]+ n[2]
        
        #Print answer
        self.totalRisk(dist)
 
#Create the class and call the dijkstra algorithm starting at 0
g = Graph(size, connections)
g.dijkstra(0)