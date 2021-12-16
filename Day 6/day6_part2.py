#Jonathan Zhao

import numpy as np
#Read input
with open('Day 6\day6_input.txt') as file:
    contents = file.readlines()
    contents = ''.join(contents)


#Organize input
#School is an array which holds the amount of fish at each stage.
school =[0,0,0,0,0,0,0,0,0]
while contents.find(',') !=-1:
    school[int(contents[:contents.find(',')])] +=1
    contents = contents[contents.find(',')+1:]
school[int(contents)] +=1 #Final value in input


#A lanternfish that creates a new fish resets its timer to 6
#A newborn lanternfish has 2 more days on its timer, starting at 8
#Estimate the amount of fish after 256 days

#Brute force won't work in this scenario


#Shift entire array down one for each day, and bring those that went to index -1 to 6, and the same amount to 8.
for day in range(256): 
    parentFish = school[0]
    for age in range(1,9): #Shifting the array down
        school[age-1] = school[age]
    #Producing more lantern fish
    school[6] = school[6] + parentFish #Parent lantern fish
    school[8] = parentFish #Newly produced lantern fish
print(school)
#Print Answer
print(sum(school))