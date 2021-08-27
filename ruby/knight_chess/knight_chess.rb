# Given two different positions on a chess board,
# find the least number of moves it would take a knight to get from one to the other. The positions will be passed as two arguments in algebraic notation. For example, knight("a3", "b5") should return 1.

# The knight is not allowed to move off the board. The board is 8x8.
def knight(start, finish)
  moves = [1, 2, -1, -2].permutation(2).to_a # all possible moves
  board = []
  (1..8).to_a.reverse.each do |letter|
    ('a'..'h').each do |number|
      board << "#{letter}#{number}"
    end
  end
  board = board.each_slice(8).to_a # board finished

end

knight(1, 2)
# https://github.com/pitchet2/Shortest-Knight-Path/blob/master/knightpath.py
