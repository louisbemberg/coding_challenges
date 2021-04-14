
def snail(array)
end
test_array = [[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]]
p snail(test_array)

def snail_recursive(array)
  # using transpose + matrix indentities + recursion
  array.empty? ? [] : array.shift + snail(array.transpose.reverse)
end

def snail_transpose(array)
  # using transpose without recursion :
  result = []
  while array.flatten.any?
    result << array.shift
    array = array.transpose.reverse
  end
  result.flatten
end


