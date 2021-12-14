#Jonathan Zhao

import numpy as np

#Read input file
with open('Day 4\day4_input.txt') as file:
    contents = file.readlines()
for value in np.arange(len(contents)): #Strips the extra space after each value
    contents[value] = contents[value].strip()

#Board Class
class board:
    #Python class variables are shared by all object instances of the class!
    def __init__(self, bingo_board): #Creates the bingo board
        self.bingo_board = [int(value) for value in bingo_board.split()] #Instance variable
        self.bingo_nums = [] #Instance variable
        self.winning_num = 0 #Instance variable

    def bingoNum(self,bingo_num): #Adds the number to the list of bingo numbers
            self.bingo_nums.append(bingo_num)
            return self.bingo(bingo_num) #Returns if there was bingo or not.

    def horizontalCheck(self, marked, mark): #Function checks the row of the marked value for a bingo.
        if mark%5 == 0: #Column 1
            markedCounter = 0
            for index in np.arange(5): #Checks the entire row based on position of marked value
                if self.bingo_board[mark+index] in self.bingo_nums:
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False
        elif mark%5 ==1: #Column 2 
            markedCounter = 0
            for index in np.arange(5): #Checks the entire row based on position of marked value
                if self.bingo_board[mark-1+index] in self.bingo_nums:
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False
        elif mark%5 ==2: #Column 3
            markedCounter = 0
            for index in np.arange(5): #Checks the entire row based on position of marked value
                if self.bingo_board[mark-2+index] in self.bingo_nums:
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False
        elif mark%5 ==3: #Column 4
            markedCounter = 0
            for index in np.arange(5): #Checks the entire row based on position of marked value
                if self.bingo_board[mark-3+index] in self.bingo_nums:
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False
        else: #Column 5
            markedCounter = 0
            for index in np.arange(5): #Checks the entire row based on position of marked value
                if self.bingo_board[mark-4+index] in self.bingo_nums:
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False

    def verticalCheck(self, marked, mark): #Checks columns for bingo
        if mark <5: #Row 1
            markedCounter = 0
            for index in np.arange(5): ##Checks the column based on position of marked value
                if self.bingo_board[mark+index*5] in self.bingo_nums: 
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False
        elif 4<mark<9: #Row 2 
            markedCounter = 0
            for index in np.arange(5): #Checks the column based on position of marked value
                if self.bingo_board[mark+(index-1)*5] in self.bingo_nums: 
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False
        elif 9<mark<14: #Row 3
            markedCounter = 0
            for index in np.arange(5): #Checks the column based on position of marked value
                if self.bingo_board[mark+(index-2)*5] in self.bingo_nums: 
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False
        elif 15<mark<19: #Row 4
            markedCounter = 0
            for index in np.arange(5): #Checks the column based on position of marked value
                if self.bingo_board[mark+(index-3)*5] in self.bingo_nums: 
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False
        else: #Row 5
            markedCounter = 0
            for index in np.arange(5): #Checks the column based on position of marked value
                if self.bingo_board[mark+(index-4)*5] in self.bingo_nums: 
                    markedCounter +=1
            if markedCounter ==5:
                return True
            else:
                return False

    def bingo(self,bingo_num):
        marked = [] #Stores the marked bingo value indexes
        for num in self.bingo_nums: #Check for marked values on the board
            if num in self.bingo_board: #Get index of any marked numbers on the board
                marked.append(self.bingo_board.index(num))
        for mark in marked: #For each index of a marked number, check for bingo
            if self.verticalCheck(marked, mark) or self.horizontalCheck(marked, mark):
                self.winning_num = bingo_num
                return True
        return False

    def score(self): #Calculates score of winning board
        unmarked = []
        for num in self.bingo_board:
            if num not in self.bingo_nums:
                unmarked.append(num)
        return sum(unmarked)*self.winning_num
    
#Bingo Number Draw
draws = contents[0].split(',')
bingo_boards = contents[2:]

#Setting up the boards:
boards = [] #List of boards
while len(bingo_boards)> 0: #While there are still boards left in the input
    boards.append(board(' '.join(bingo_boards[:5]))) #Create a board and add it to the list of boards
    bingo_boards = bingo_boards[6:]

#Drawing numbers:
bingo = False
draw_number = 0
score = 0
while bingo == False: #While there are no bingos
    for bingo_board in boards: #Draw a number and check each board for bingo
        if bingo_board.bingoNum(int(draws[draw_number])): #If there is a bingo
            bingo = True
            score = bingo_board.score() #Get score of winning board
    draw_number+=1
    
#Print answer
print('Bingo Answer: ',score)
