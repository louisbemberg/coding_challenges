def solution(a):
    # technically not necessary, but saving len(a) in a variable
    n = len(a)
    # creating a target matrix so I can plug numbers backwards without worrying about index out of range
    b = [[0]*n for i in range(0,n)]
    # Iterating from 3=>0 for a 4x4 matrix, as I will fill the matrix from top right to bottom right
    for i in reversed(range(0, n)):
        # Iterating on each row and keeping track of the index of the number
        # the old column of the number will be the new row of the number
        for index, number in enumerate(a[n-i-1]):
            # In the new matrix, assign as row the column of the new number
            b[index][i] = number
            print(b)

    return b


# Let's follow an example.
a = [['A','B', 'C'],
     ['D', 'E', 'F'],
     ['G', 'H', 'I']]

# We iterate from 2=>0, then for each of those iterations we iterate on each row of the matrix a, such that:
# i=2 & row1['A','B', 'C'], i=2 & row2[D,E,F], i=2 & row3[G,H,I], i=1 & row1, etc..
# For the first & first iterations, we are looking at row1[0]('A') with i=2.
# next, we say that the INDEX (left-right coordinate) of 'A', which is 0, is now it's (top-bottom) coordinate
# so we're looking at b[0]
# since we want 1 to be all the way to the right, here comes our descending i=2.
# this gives us  b[0][2] (or b[index][i])
# what value do we assign that number? the one we're currently iterating on.
# b[0][2] = 'A' (or b[index][i] = number)
# we repeating the operation for the number below, which means we keep i=2 but use the next index, the number 2 with index 1:
# b[1][2] = 'B'
# and we keep going. 




a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

b = [[1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]]

solution(a)
print('-------')
solution(b)