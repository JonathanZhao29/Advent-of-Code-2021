#Jonathan Zhao's Code

#Read input
with open('Day 10\day10_input.txt') as file:
    contents = file.readlines()



#Stack to find the corrupted line
def findMissing(line):
    syntaxStack = []
    corrupt =''
    points = 0
    for syntax in line:
        #If open symbol, add its counterpart to the stack
        if syntax == '(':
            syntaxStack.append( ')')
        elif syntax == '[':
            syntaxStack.append(']')
        elif syntax == '{':
            syntaxStack.append('}')
        elif syntax == '<' :
            syntaxStack.append('>')
        else: #Closure symbol
            if syntax == syntaxStack[-1]: #If closure symbol is on the top of the stack
                syntaxStack.pop()
            else: #Closure symbol is corrupt
                corrupt = syntax
                break
    if corrupt =='': #If not corrupted, find missing
        syntaxStack.reverse()
        print(syntaxStack)
        pointSystem = {')':1, ']':2,'}':3,'>':4} #Point system
        for syntax in syntaxStack: #Add points
            points *= 5
            points +=pointSystem[syntax]
    return points



pointSystem = {'':0,')':3, ']':57,'}':1197,'>':25137} #Values for each symbol

points =[] #Syntax Points
for line in contents: #For each line of input
    missing = findMissing(line.strip())
    if missing !=0: #If the line has missing
        points.append(missing) #Find the corrupted syntax

#Sort points and find middle value
points.sort()
answer = points[int(len(points)/2)]
#Print Answer
print(answer)