# Your task, is to create a NxN spiral with a given size.

# For example, spiral with size 5 should look like this:

# 00000
# ....0
# 000.0
# 0...0
# 00000
# and with the size 10:

# 0000000000
# .........0
# 00000000.0
# 0......0.0
# 0.0000.0.0
# 0.0..0.0.0
# 0.0....0.0
# 0.000000.0
# 0........0
# 0000000000
# Return value should contain array of arrays, of 0 and 1, for example for given size 5 result should be:

# [[1,1,1,1,1],[0,0,0,0,1],[1,1,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Because of the edge-cases for tiny spirals, the size will be at least 5.

# General rule-of-a-thumb is, that the snake made with '1' cannot touch to itself.

require 'pry-byebug'

NEXT_DIRECTION = {
  'r' => 'd',
  'd' => 'l',
  'l' => 'u',
  'u' => 'r'
}
def spiralize(size)
  spiral = create_grid(size)
  # see create_grid. we start at bottom left going up with edges done.
  direction = 'u'
  x = 0
  y = size - 1
  until spiral_finished?(spiral, x, y, direction)
    # binding.pry
    if can_keep_going?(spiral, x, y, direction)
      coordinates = new_coordinates(x, y, direction)
      x = coordinates[0]
      y = coordinates[1]
      spiral[y][x] = 1
    else
      direction = NEXT_DIRECTION[direction]
    end
  end
  spiral
end

def create_grid(size)
  # creates grid with first edges done.
  # example with size 4:
  # 1 1 1 1
  # 0 0 0 1
  # 0 0 0 1
  # 1 1 1 1
  spiral = []
  size.times do
    spiral << ([0] * (size - 1)) + [1]
  end
  spiral[0] = [1] * size
  spiral[size - 1] = [1] * size
  spiral
end

def can_keep_going?(grid, x, y, direction)
  case direction
  when 'r'
    ![1, nil].include?(grid[y][x + 2])
  when 'd'
    ![1, nil].include?(grid[y + 2][x])
  when 'l'
    ![1, nil].include?(grid[y][x - 2])
  when 'u'
    ![1, nil].include?(grid[y - 2][x])
  end
end

def new_coordinates(x, y, direction)
  case direction
  when 'r'
    x += 1
  when 'd'
    y += 1
  when 'l'
    x -= 1
  when 'u'
    y -= 1
  end
  [x, y]
end

def spiral_finished?(spiral, x, y, direction)
  # FIGURE OUT THE CONDITION FOR WHICH THE SPIRAL IS DONE
end
# grid = [[1,1,1,1,1],[0,0,0,0,1],[0,0,0,0,1],[0,0,0,0,1],[1,1,1,1,1]]
# answer = spiralize(10)

incomplete = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

incomplete = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
[1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
[1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
[1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

puts spiral_finished?(a, 2, 7, 'u')
