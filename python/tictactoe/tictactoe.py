# https://www.codewars.com/kata/5b817c2a0ce070ace8002be0/train/python

# build a function, which, given a list  and a width, returns a tic-tac-toe style grid:
# input: ["O", "X", " ", " ", "X", " ", "X", "O", " "]
# output: 
# O | X |   
# -----------
#    | X |   
# -----------
#  X | O |   

# input: ["O", "X", " ", " ", "X", " ", "X", "O", " ", "O"]
# output: 
#  O | X |   |   | X 
# -------------------
#    | X | O |   | O 

def build_row(row):
    return f' {" | ".join(row)} '

def display_board(board, width):
    #your code here
    rows = []
    for i in range(0, len(board), width):
        rows.append(board[i:i+width])
    separator = f"\n{'-'*(3*width + width - 1)}\n"
    return separator.join([build_row(row) for row in rows])

print(display_board(["O", "X", " ", " ", "X", " ", "X", "O", " "], 3))
print(display_board(["O", "X", "X", "O"],2))