#Jonathan Zhao's Code

#Function that returns 1 for increase, 0 for decrease
def depthIncr(depth1, depth2):
    if depth1 ==0: #N/A measurement on first depth value
        return 0
    elif depth1 < depth2: #If there is an increase
        return 1
    else: #No increase
        return 0

#Read input file
with open('day1_input.txt') as file:
    contents = file.readlines()

#Loop through input and count increases
increases = 0
depth1 = 0 #Initial depth
for line in contents:  #For each depth value in input
    depth2 = int(line) 
    increases += depthIncr(depth1, depth2) #Compare the current depth value with the previous value
    depth1 = depth2

#Total increases:
print(increases)