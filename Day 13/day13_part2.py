#Jonathan Zhao's Code
import matplotlib.pyplot as plt
#Read input
with open('Day 13\day13_input.txt') as file:
    contents = file.readlines()

#Format coordinate input
coords = []
for coordinate in contents[:contents.index('\n')]:
    coords.append(coordinate.strip())
#Format into tuple pairs
coords = [tuple([int(coord[:coord.find(',')]),int(coord[coord.find(',')+1:])]) for coord in coords]

#Format folding directions
directions = []
for direction in contents[contents.index('\n')+1:]:
    directions.append(direction[11:].strip())
directions = [tuple([direction[:direction.find('=')],int(direction[direction.find('=')+1:])]) for direction in directions]


#Folding function
def fold(direction, coords):
    #Split in two, x or y
    if direction[0] =='x': #If fold on x axis
        for coord in range(len(coords)):
            #if coord is bigger than the direction number
            if coords[coord][0] > direction[1]:
                coords[coord] = tuple([direction[1] - (coords[coord][0]-direction[1]),coords[coord][1]]) #Fold the coord
    else:#If fold on y axis
        for coord in range(len(coords)):
            #if coord is bigger than the direction number
            if coords[coord][1] > direction[1]:
                coords[coord] = tuple([coords[coord][0],direction[1] -(coords[coord][1]-direction[1])]) #Fold the coord


#Call fold function, and remove repeated elements
for direction in directions:
    fold(direction,coords)
    coords = list(set(coords))

#Plot Answer
x_coords = [coord[0] for coord in coords]
x_bounds = [-(min(x_coords)+20), max(x_coords)+20] #Bounds for the x coordinates
y_coords = [-coord[1] for coord in coords] #Since y coords are reversed, negate them
y_bounds = [(min(y_coords)+20), -(max(y_coords)+20)] #Bounds for the y coordinates
plt.scatter(x_coords, y_coords, color = 'red') #Plot the x/y coordinates
plt.scatter(x_bounds, y_bounds, color = 'blue') #Plot the bounds to examine the points
plt.show() #Show the plot

