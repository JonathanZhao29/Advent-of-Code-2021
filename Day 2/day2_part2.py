#Jonathan Zhao's Code

#Read input file
with open('Day 2\day2_input.txt') as file:
    contents = file.readlines()

class submarine: #Class that holds the horizontal position, depth, and aim values of a submarine
    #Position values
    horizontal = 0
    depth = 0
    aim = 0

    def __init__(self, horizontal, depth, aim): #Constructor
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim
    def travel_forward(self, horizontal): #Horizontal movement and depth
        self.horizontal +=horizontal
        self.depth = self.depth + self.aim*horizontal
    def travel_vertical(self, aim): #Changes aim value
        self.aim +=aim
    def position(self): #Report current position
        return (self.horizontal * self.depth)



def travel(direction, distance, submarine): #Function that sends direction and distance to submarine
    if direction == 'forward':
        submarine.travel_forward(distance)
    elif direction =='up':
        submarine.travel_vertical(-distance)
    else:
        submarine.travel_vertical(distance)


elf_sub = submarine(0,0,0)
for line in contents: #Loops through every line of input
    split = line.find(' ')
    direction = line[:split]
    distance = int(line[split:])
    travel(direction, distance, elf_sub )


#Answer
print(elf_sub.position())




