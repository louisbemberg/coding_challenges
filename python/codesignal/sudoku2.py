
def valid_sudoku(subgrid):
    numbers = [x for x in subgrid if x != '.']
    # checking duplicates
    condition1 = len(numbers) == len(set(numbers))
    # checking 1..9 only
    condition2 = all(int(i) >= 1 and int(i) <= 9 for i in numbers)
    return condition1 and condition2

def solution(grid):
    # rows
    test1 = all(valid_sudoku(row) for row in grid)
    # columns
    columns = []
    for i in range(0,9):
        columns.append([row[i] for row in grid])
    test2 = all(valid_sudoku(column) for column in columns)
    # 3x3 squares
    squares = []
    for i in [0, 3, 6]:
        for j in [0, 3, 6]:
            squares.append(grid[i][j:j+3] + grid[i+1][j:j+3] + grid[i+2][j:j+3])
    test3 = all(valid_sudoku(square) for square in squares)

    return test1 and test2 and test3

# Optimal Solution
def solution(grid):
    for i in range(9):
        for j in range(9):
            num = grid[i][j]
            if num != '.':
                for k in range(9):
                    if k != j and grid[i][k] == num:
                        return False
                    if k != i and grid[k][j] == num:
                        return False
                    top_i = i - i%3
                    top_j = j - j%3
                    if (top_i+k//3,top_j+k%3) != (i,j) and grid[top_i+k//3][top_j+k%3] == num:
                        return False

    return True

goodgrid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]

badgrid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]


badgrid2 = [[".",".","4",".",".",".","6","3","."], 
 [".",".",".",".",".",".",".",".","."], 
 ["5",".",".",".",".",".",".","9","."], 
 [".",".",".","5","6",".",".",".","."], 
 ["4",".","3",".",".",".",".",".","1"], 
 [".",".",".","7",".",".",".",".","."], 
 [".",".",".","5",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."], 
 [".",".",".",".",".",".",".",".","."]]

print(solution(goodgrid))
print(solution(badgrid))
print(solution(badgrid2))