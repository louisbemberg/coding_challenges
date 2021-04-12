# Implement a method that will check if a sudoku grid is valid.
# the method receives an array containing 9 arrays of size 9.
# rule 1: 3x3 squares must contain every digit only once
# a row must contain every digit exactly once
# a column must contain every digit exactly once

def valid_sudoku?(array)
  sudo_row?(array) && sudo_column?(array) && sudo_blocks?(array) && blank_cells?(array)
end

def sudo_row?(array)
  array.all? { |a| a.uniq.size == 9 }
end

def sudo_column?(array)
  array.transpose.all? { |a| a.uniq.size == 9 }
end

def sudo_blocks?(array)
  block_rows = []
  3.times do |k|
    [0, 3, 6].each do |i|
      [0, 1, 2].each do |j|
        block_rows << array[j + (3 * k)][i..(i + 2)]
      end
    end
  end
  blocks = block_rows.each_slice(3).to_a
  blocks.all? do |block|
    block.flatten.uniq.size == 9
  end
end

def blank_cells?(array)
  !array.flatten.include?(0)
end

p valid_sudoku?([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 5, 3, 4, 8],
  [1, 9, 8, 3, 4, 2, 5, 6, 7],
  [8, 5, 9, 7, 6, 1, 4, 2, 3],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 6, 1, 5, 3, 7, 2, 8, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 4, 5, 2, 8, 6, 1, 7, 9]
]) # => true

p valid_sudoku?([
  [5, 3, 4, 6, 7, 8, 9, 1, 2],
  [6, 7, 2, 1, 9, 0, 3, 4, 8],
  [1, 0, 0, 3, 4, 2, 5, 6, 0],
  [8, 5, 9, 7, 6, 1, 0, 2, 0],
  [4, 2, 6, 8, 5, 3, 7, 9, 1],
  [7, 1, 3, 9, 2, 4, 8, 5, 6],
  [9, 0, 1, 5, 3, 7, 2, 1, 4],
  [2, 8, 7, 4, 1, 9, 6, 3, 5],
  [3, 0, 0, 4, 8, 1, 1, 7, 9]
]) # => false

p valid_sudoku?([
  [7, 2, 6, 4, 9, 3, 8, 1, 5],
  [3, 1, 5, 7, 2, 8, 9, 4, 6],
  [4, 8, 9, 6, 5, 1, 2, 3, 7],
  [8, 5, 2, 1, 4, 7, 6, 9, 3],
  [6, 7, 3, 9, 8, 5, 1, 2, 4],
  [9, 4, 1, 3, 6, 2, 7, 5, 8],
  [1, 9, 4, 8, 3, 6, 5, 7, 2],
  [5, 6, 7, 2, 1, 4, 3, 8, 9],
  [2, 3, 8, 5, 7, 9, 4, 6, 1]
]) # => true


# # Block # 0
#  array[0][0..2]
#  array[1][0..2]
#  array[2][0..2]
# # Block # 1
#  array[0][3..5]
#  array[1][3..5]
#  array[2][3..5]
# # Block # 2
#  array[0][6..8]
#  array[1][6..8]
#  array[2][6..8]
# # Block # 3
#  array[3][0..2]
#  array[4][0..2]
#  array[5][0..2]
# # Block # 4
#  array[3][3..5]
#  array[4][3..5]
#  array[5][3..5]
# # Block # 5
#  array[3][6..8]
#  array[4][6..8]
#  array[5][6..8]
# # Block # 6
#  array[6][0..2]
#  array[7][0..2]
#  array[8][0..2]
# # Block # 7
#  array[6][3..5]
#  array[7][3..5]
#  array[8][3..5]
# # Block #  8
#  array[6][6..8]
#  array[7][6..8]
#  array[8][6..8]
