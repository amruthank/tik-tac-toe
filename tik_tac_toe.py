import os
import sys
import random
import time

board = {'topL' : '', 'topM' : '', 'topR' : '',
         'midL' : '', 'midM' : '', 'midR' : '',
         'lowL' : '', 'lowM' : '', 'lowR' : ''}

def print_board():

    print("\n=============\n")
    print(board['topL']+ '  | ' +board['topM']+ '  | ' +board['topR'])
    print('- + - + -')
    print(board['midL']+ '  | ' +board['midM']+ '  | ' +board['midR'])
    print('- + - + -')
    print(board['lowL']+ '  | ' +board['lowM']+ '  | ' +board['lowR'])
    print("\n============")


def is_completion(char):
    user = "Bot"
    if char == 'X':
        user = "Human"
        
    i = 0
    i = int(i)
    while(i<9):
        count = 0
        for j in range(0,3):
           
            if board[list(board)[i]] != '' and board[list(board)[i]] != char:
                 i = i + (3 - j)
                 count = 0
                 break
            elif board[list(board)[i]] != '' and board[list(board)[i]] == char:
                 count = count + 1
                 i = i + 1
            else:
                i = i + 1

        if count == 3:
            print("%s is a winner!!"%user)
            return True
    return False        


def is_empty_dict():

    for key in board:
        if board[key] == "":
            return True


def bot():
    
    i = 0
    while(i<9):
        count = 0
       
        for j in range(0,3):
            if board[list(board)[i]] == "O":
                    count = count + 1
            elif board[list(board)[i]] == "" and i < 7:
                    if (count == 2) or (board[list(board)[i+1]] == "O" and board[list(board)[i+2]] == "O") or (board[list(board)[i-1]] == "O" and board[list(board)[i+1]] == "O"):
                        _assign_value(list(board)[i],"O")
                        return True
            i = i + 1
            
                              
    i = 0
    while(i<9):
        count = 0
        for j in range(0,3):
            if board[list(board)[i]] == "X":
                count = count + 1
            elif board[list(board)[i]] == "" and i<7:
                if (count == 2) or (board[list(board)[i+1]] == "X" and board[list(board)[i+2]] == "X") or (board[list(board)[i-1]] == "X" and board[list(board)[i+1]] == "X"):
                    _assign_value(list(board)[i],"O")
                    return True
            i = i + 1

    i = 0
    while(i<9):
        count = 0
        
        for j in range(0,3):
            if board[list(board)[i]] == "O":
                    count = count + 1
            elif board[list(board)[i]] == "" and i < 7:
                    if (count == 1) or (board[list(board)[i+1]] == "" and board[list(board)[i+2]] == "") or (board[list(board)[i-1]] == "" and board[list(board)[i+1]] == ""):
                        _assign_value(list(board)[i],"O")
                        return True
            i = i + 1        
            
    while is_empty_dict():
        rand = random.randint(0,8)
        if board[list(board)[rand]] == "":
            _assign_value(list(board)[i],"O")
            return True
    
    print("Both are the loosers!!:P")
    return False

def _is_dict_value_empty(value):
    return (board[value] == "")

def _assign_value(key,value):
    board[key] = value
    
def main():

    while is_empty_dict():
        print_board()
        val = input("Enter the position: ")
        if _is_dict_value_empty(val):
            _assign_value(val,"X")
            if is_completion('X'):
                return True
            print_board()
            time.sleep(1)
            if not bot():
                return True
            if is_completion('O'):
                return True



if __name__ == '__main__':
    main()
