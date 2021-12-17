#Jonathan Zhao's Code

#Read input
with open('Day 8\day8_input.txt') as file:
    contents = file.readlines()

    outputs = [line[line.find('|')+1:].strip()for line in contents] #Format input to only contain output values

#In the output values, how many times do digits 1,4,7 or 8 appear?
count = 0
for output in outputs: #For each line
    while len(output) !=0:
        if output.find(' ') !=-1: #Spaces seperate all of the output values on one line
            value = output[:output.find(' ')]
            output = output[output.find(' ')+1:]
        else: #Last output value on the line
            value = output
            output = ''
        if len(value) == 2 or len(value) == 3 or  len(value) == 4 or len(value) == 7: #If 1,4,7 or 8
            count+=1

#Print Answer
print('Correct digits:', count)
    