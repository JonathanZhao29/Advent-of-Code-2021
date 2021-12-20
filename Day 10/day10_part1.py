#Jonathan Zhao's Code

#Read input
with open('Day 10\day10_input.txt') as file:
    contents = file.readlines()



#Stack to find the corrupted line
def findCorrupted(line):
    syntaxStack = []
    corrupt =''
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
    return corrupt

pointSystem = {'':0,')':3, ']':57,'}':1197,'>':25137} #Values for each symbol

points = 0 #Syntax Points
for line in contents: #For each line of input
    
    corrupt = findCorrupted(line.strip()) #Find the corrupted syntax
    points += pointSystem[corrupt] #Add the points for the corrupt syntax

#Print Answer
print(points)