#Jonathan Zhao's Code

#Function which compares two depth windows, which returns 1 for increase, 0 for decrease
def depthSumIncr(depth1, depth2):
    if depth1 ==0: #N/A measurement on first depth window
        return 0
    elif depth1 < depth2: #If there is an increase
        return 1
    else: #No increase
        return 0

#Read input file
with open('Day 1\day1_input.txt') as file:
    contents = file.readlines()

#Loop through input and count increases
increases = 0
depth1 = int(contents[0])+int(contents[1])+int(contents[2]) #Initial depth window
index = 1
while index+2<len(contents): #While there are enough values for the sliding window
    depth2 = int(contents[index])+int(contents[index+1])+int(contents[index+2]) 
    increases += depthSumIncr(depth1, depth2) #Compare the current depth value window with the previous window
    depth1 = depth2
    index+=1

#Total increases:
print(increases)