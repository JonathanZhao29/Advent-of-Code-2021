#Jonathan Zhao
import numpy as np

with open('Day 5\day5_input.txt') as file:
    contents = file.readlines()
for value in range(len(contents)): #Strips the extra space after each value
    contents[value] = contents[value].strip()


#Function to calculate each point in a line and returns an array of those points
def calcLine(line):
    #Format the line
    x1 = int(line[:line.find(',')])
    y1 = int(line[line.find(',')+1:line.find(' ')])
    line = line[line.find('>')+1:]
    x2 = int(line[:line.find(',')])
    y2 = int(line[line.find(',')+1:])

    points = [] # x,y
    if x1 == x2: #Vertical Line
        if y1 < y2:
            for segment in range(y2-y1+1): #For each point, append it to the list of points
                point = str(x1)+','+str((y1+segment))
                points.append(point)
        else:
            for segment in range(y1-y2+1): #For each point, append it to the list of points
                point = str(x1)+','+str((y2+segment))
                points.append(point)
    elif y1 == y2: #Horizontal Line
        if x1 < x2: 
            for segment in range(x2-x1+1): #For each point, append it to the list of points
                point = str(x1+segment)+','+str(y1)
                points.append(point)
        else:
            for segment in range(x1-x2+1): #For each point, append it to the list of points
                point = str(x2+segment)+','+str(y1)
                points.append(point)
    else: #Diagonal line
        for segment in range(abs(x1-x2)+1): #If 45 degree diagonal, the abs distance between x1,x2 and y1,y2 are the same
            if x1>x2: 
                if y1>y2:
                    point = str(x2+segment) + ',' + str(y2+segment) #Calculates each point on the diagonal
                    points.append(point)
                else:
                    point = str(x2+segment) + ',' + str(y2-segment) #Calculates each point on the diagonal
                    points.append(point)
            else:
                if y1>y2:
                    point = str(x1+segment) + ',' + str(y1-segment) #Calculates each point on the diagonal
                    points.append(point)
                else:
                    point = str(x1+segment) + ',' + str(y1+segment) #Calculates each point on the diagonal
                    points.append(point)

    return points

#Create a dictionary, then calculate where each line is and add each point in the line to the dict to count overlaps.
lines = {}
for line in contents:
    points = calcLine(line)
    for point in points:
        if point in lines: #If the point is already in the dict, increase the overlap value by 1
            lines[point] +=1
        else: #Add the point to the dict, and set its overlap value to 1
            lines[point] = 1

#Go through the dictionary and count every point where the overlap value was 2 or larger.
overlap = 0
for line in lines:
    if lines[line] >=2:
        overlap+=1

#Print answer
print('overlaps:',overlap)