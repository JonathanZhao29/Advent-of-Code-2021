#Jonathan Zhao's Code

#Read input
with open('Day 8\day8_input.txt') as file:
    contents = file.readlines()
    inputs = [line[:line.find('|')]for line in contents]
    outputs = [line[line.find('|')+1:].strip()for line in contents] #Format input to only contain output values


def stringToArr(string):
    value = []
    while len(string) !=0:
        if string.find(' ') !=-1: #Spaces seperate all of the output values on one line
            value.append(string[:string.find(' ')])
            string = string[string.find(' ')+1:]
        else: #Last output value on the line
            value.append(string)
            string = ''
    return value

def inCommon(string1, string2):
    return len(list(set(''.join(sorted(string1)))&set(''.join(sorted(string2)))))

def setupSegments(inputSegments): #Returns a dictionary with the segment number as key and pattern as value
    values = stringToArr(inputSegments)
    segmentPattern = {}
    #Setup the initial 4 unique patterns
    counter = 0
    while len(values) >counter:
        pattern = values[counter]
        if len(pattern) == 2:#One
            segmentPattern[''.join(sorted(pattern))] = 1
            one = ''.join(sorted(pattern))
            values.remove(pattern)
        elif len(pattern) == 3:#Seven
            segmentPattern[''.join(sorted(pattern))] = 7
            values.remove(pattern)
        elif len(pattern) == 4:#Four
            segmentPattern[''.join(sorted(pattern))] = 4
            values.remove(pattern)
            four = ''.join(sorted(pattern))
        elif len(pattern) == 7:#Eight
            segmentPattern[''.join(sorted(pattern))] = 8
            values.remove(pattern)
        else:
            counter +=1

    #Setup the remaining patterns
    while len(values) !=0:
        pattern = values[0]
        if len(pattern) ==5: #2,3,5 all have a length of 5
            common = inCommon(four,pattern) #5 has 3 segments in common with 4, while 2 has 2 segments in common with 4
            if common == 3 and inCommon(one,pattern) == 1: #5
                segmentPattern[''.join(sorted(pattern))] = 5
                values.remove(pattern)
            elif common ==2: #2
                segmentPattern[''.join(sorted(pattern))] = 2
                values.remove(pattern)
            else: #3
                segmentPattern[''.join(sorted(pattern))] = 3
                values.remove(pattern)
        else : #Remaining length is 6, which contain 0,6,9
            if inCommon(four,pattern)== 4: #9 contains all of 4's segments
                segmentPattern[''.join(sorted(pattern))] = 9
                values.remove(pattern)
            elif inCommon(one,pattern) ==1:#6 contains only one segment in common with 1
                segmentPattern[''.join(sorted(pattern))] = 6
                values.remove(pattern)       
            else: #0
                segmentPattern[''.join(sorted(pattern))] = 0
                values.remove(pattern)
    #Segment patterns have been setup
    return segmentPattern

outputTotal = 0
for line in range(len(contents)):
    inputSegments = setupSegments(inputs[line]) #Setup inputs and their corresponding values
    outputArr = stringToArr(outputs[line])#Change the output line to an array with 4 values
    outputValue =0 #The output value of that line
    for output in range(3,-1,-1):
        outputValue += (inputSegments[''.join(sorted(outputArr[3-output]))]) * (10**output) #Sets up the place values ex: 1000,100,10,1
    outputTotal +=outputValue


#Print Answer
print('Total output value',outputTotal)