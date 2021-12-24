#Jonathan Zhao's Code
from collections import Counter #Used to count most common and least common elements
#Read input
with open('Day 14\day14_input.txt') as file:
    contents = file.readlines()

#Clean input and set up insertion pairs dictionary
polymer = list(contents[0].strip())
insertion_pairs = {}
for line in range(2,len(contents)): #Sets up dictionary of insertion pairs
    pair = contents[line][:contents[line].find('->')-1]
    insert = contents[line][contents[line].find('->')+2:].strip()
    insertion_pairs[pair] = insert

#Insertion function 
def insertion(polymer, insertion_pairs): #Takes the polymer and dictionary of insertion pairs, returns new polymer with inserts
    new_polymer = [] 
    insertion_index = 1
    while insertion_index <len(polymer): #For each 2 polymer pair, append the insertion polymer inbetween them
        poly_insert = insertion_pairs[polymer[insertion_index-1]+polymer[insertion_index]]
        new_polymer.append(polymer[insertion_index-1])
        new_polymer.append(poly_insert)
        insertion_index+=1
    new_polymer.append(polymer[-1]) #Append the last value in the old polymer
    return new_polymer

#10 steps
for step in range(10):
    polymer = insertion(polymer, insertion_pairs)

#Find most common and least common element and their count using Counter
poly_count = Counter(polymer)
most_common = poly_count.most_common()[0][1]
least_common = poly_count.most_common()[-1][1]
answer = most_common-least_common
#Print Answer
print(answer)