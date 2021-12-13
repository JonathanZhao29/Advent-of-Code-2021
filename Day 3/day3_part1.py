#Jonathan Zhao's Code
import numpy as np
#Read input file
with open('Day 3\day3_input.txt') as file:
    contents = file.readlines()

#Figure out the number of ones for each column of the input
ones = np.repeat(0,len(contents[0])-1) #Array of zeros at the same length as an input
for line in contents:
    for digit in np.arange(len(line)): #For each digit in the line of input, add to the ones array if = 1
        if line[digit] == '1':
            ones[digit] +=1
#Calculate the gamma and epsilon rate
gamma_rate, epsilon_rate = '',''
print(ones)
for digits in np.arange(len(contents[0])-1):#For each digit in the line of input, determine which bit is most common and least common
    if len(contents) - ones[digits] > ones[digits]: #If the bit 0 is more common
        gamma_rate +='0'
        epsilon_rate +='1'
    else: #If the bit 1 is more common
        gamma_rate +='1'
        epsilon_rate +='0'

#Calculating the final answer
output = int(gamma_rate,2) *int(epsilon_rate,2)
print(output)