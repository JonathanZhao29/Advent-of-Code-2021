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

#Create 2 dictionaries
#One to track the number of times different combinations that appear in the polymer, adds to itself each step
#One to track the number of times each polymer letter appears
#Loop 40 times through first dictionary, and track the increase of polymer letters in the second dictionary

#Function to add values to a dictionary
def add_sequence(polymer, dictionary,increase=1):
    if polymer in dictionary: #If it exists in the dict, increase the dict value by one
        dictionary[polymer] +=increase
    else: #If it does not exist in the dict, create a new key with value = one
        dictionary[polymer] =increase

#Create 2 dictionaries
#One to track the number of times different combinations that appear in the polymer, adds to itself each step
#One to track the number of times each polymer letter appears
letter_count = {}
combinations = {}
#Input the initial polymer in to the combinations dictionary, and the letters into the letter_count dictionary
insertion_index = 1
while insertion_index <len(polymer): #For each 2 polymer pair, track their counts
    poly_insert = polymer[insertion_index-1]+polymer[insertion_index]
    add_sequence(poly_insert, combinations)
    insertion_index +=1
for letter in polymer:
    add_sequence(letter, letter_count)


#Run through 40 steps
for step in range(40):
    #Go through combinations dictionary, get newly made combinations count letters
    new_combinations = {}
    for pair in combinations: #For each polymer pair in combinations
        insert_letter = insertion_pairs[pair] #Get the insertion letter for that pair
        num_pairs = combinations[pair] #Amount of original pairs
        #Add that letter to the letter_count dictionary for the amount of original pairs
        add_sequence(insert_letter, letter_count, combinations[pair])
        #Create new polymer pairs using the insertion letter
        new_pair1 = pair[0]+insert_letter
        new_pair2 = insert_letter+pair[1]
        #Add the 2 new pairs to a seperate dictionary for the amount of original pairs
        add_sequence(new_pair1,new_combinations, num_pairs)
        add_sequence(new_pair2,new_combinations, num_pairs)
    combinations = new_combinations

#Get most common and least common:
most_common = Counter(letter_count).most_common()[0][1]
least_common = Counter(letter_count).most_common()[-1][1]

answer = most_common-least_common
#Print Answer
print('difference between most common and least common:',answer)