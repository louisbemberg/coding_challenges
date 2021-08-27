# Inspired from Codewars' Snails

# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:

# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]


# for a 3 x 3
  # 1 2 3 array[0]
  # 4 5 6 array[1]
  # 7 8 9 array[2]

  # array[0][0] start
  # array[0][1] right
  # array[0][2] right
  # array[1][2] down
  # array[2][2] down
  # array[2][1] left left
  # array[2][0] up
  # array[1][0]
  # array[1][1]

    # Pattern: Starting at [0][0],
  # we go N - 1 times to the right
  # we go N - 1 times down
  # we go N - 1 times to the left

  # we go N - 2 times up
  # we go N - 2 times right
  # we go N - 3 times down
  # we go N - 3 times left

  # for a 4 x 4
  # 1  2  3  4 array[0]
  # 12 13 14 5 array[1]
  # 11 16 15 6 array[2]
  # 10 9  8  7 array[3]

  # array[0][0] start

  # array[0][1] right
  # array[0][2] right
  # array[0][3] right

  # array[1][3] down
  # array[2][3] down
  # array[3][3] down

  # array[3][2] left
  # array[3][1] left
  # array[3][0] left

  # array[2][0] up
  # array[1][0] up

  # array[1][1] right
  # array[1][2] right

  # array[2][2] down

  # array[2][1] left


  # Pattern: Starting at [0][0],
  # we go N - 1 times to the right
  # we go N - 1 times down
  # we go N - 1 times to the left

  # we go N - 2 times up
  # we go N - 2 times right
  # we go N - 3 times down
  # we go N - 3 times left
