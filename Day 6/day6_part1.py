#Jonathan Zhao


#Read input
with open('Day 6\day6_input.txt') as file:
    contents = file.readlines()
    contents = ''.join(contents)
#Organize input
timers = []
while contents.find(',') !=-1:
    timers.append(int(contents[:contents.find(',')]))
    contents = contents[contents.find(',')+1:]
timers.append(int(contents)) #Final value in input

#A lanternfish that creates a new fish resets its timer to 6
#A newborn lanternfish has 2 more days on its timer, starting at 8
#Estimate the amount of fish after 80 days

#Brute Force Method

#Set up initial school of lanternfish
school = []
for timer in timers:
    school.append(timer)

#Simulate 80 days
for day in range(80):
    for timer in range(len(school)):
        school[timer] -=1
        if school[timer] <0:
            school[timer] = 6
            school.append(8)

#Print answer
print(len(school))
