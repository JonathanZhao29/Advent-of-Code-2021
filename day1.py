#Jonathan Zhao's Code

#Function that returns 1 for increase, 0 for decrease
def depthIncr(depth1, depth2):
    if depth1 ==0:
        return 0
    elif depth1 < depth2:
        return 1
    else:
        return 0

#Read input file
with open('day1_input.txt') as file:
    contents = file.readlines()

#Loop through input and count increases
increases = 0
depth1 = 0
for line in contents:
    depth2 = int(line)
    increases += depthIncr(depth1, depth2)
    depth1 = depth2

#Total increases:
print(increases)