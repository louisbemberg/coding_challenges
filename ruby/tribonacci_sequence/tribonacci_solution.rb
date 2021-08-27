# a Fibonacci sequence takes the last 2 elements of a list
# and adds them together to get the next element on the list
# ex: [1, 2] => [1, 2, 3] => [1, 2, 3, 5] => [1, 2, 3, 5, 8]

# For this exercise, we will look at "Tribonacci", same concept except
# we add the last THREE elements to get the next one.
# [1, 2, 3] => [1, 2, 3, 6] => [1, 2, 3, 6, 11] => [1, 2, 3, 6, 11, 20]

# GOAL: Build a method that takes two parameters: an array, and n
# the method needs to return a tribonacci list of size n
# special cases: return [] if n is zero
# return the first n characters of the list if n <= 3
# the inital list given will always be 3 characters

# solution 1, using recursion
def tribonacci2(array, n)
  return [] if n.zero?
  return array if array.length < 3
  return array.first(n) if n <= 3

  array << array.last(3).sum
  tribonacci(array, n) if array.length < n
  array
end

# solution 2, simpler approach, abusing the property of .slice(a, b)
def tribonacci(array, n)
  (3..n).each do |i|
    array[i] = array.last(3).sum
  end
  array.slice(0, n)
end

# TESTS - RUN THE FILE TO GET FEEDBACK :)
print 'Test 1 - '
puts tribonacci([1, 1, 1], 10) == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105] ? '✅' : '❌'
print 'Test 2 - '
puts tribonacci([0, 0, 1], 10) == [0, 0, 1, 1, 2, 4, 7, 13, 24, 44] ? '✅' : '❌'
print 'Test 3 - '
puts tribonacci([0, 1, 1], 10) == [0, 1, 1, 2, 4, 7, 13, 24, 44, 81] ? '✅' : '❌'
print 'Test 4 - '
puts tribonacci([1, 0, 0], 10) == [1, 0, 0, 1, 1, 2, 4, 7, 13, 24] ? '✅' : '❌'
print 'Test 5 - '
puts tribonacci([0, 0, 0], 10) == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] ? '✅' : '❌'
print 'Test 6 - '
puts tribonacci([1, 2, 3], 10) == [1, 2, 3, 6, 11, 20, 37, 68, 125, 230] ? '✅' : '❌'
print 'Test 7 - '
puts tribonacci([3, 2, 1], 10) == [3, 2, 1, 6, 9, 16, 31, 56, 103, 190] ? '✅' : '❌'
print 'Test 8 - '
puts tribonacci([1, 1, 1], 1) == [1] ? '✅' : '❌'
print 'Test 9 - '
puts tribonacci([300, 200, 100], 0) == [] ? '✅' : '❌'
