# Write a program that prints all the integers from 1 to 100.
# Here's the trick though:
# You are not allowed to have numbers on your code.
# For example, the following lines are not valid:
# number = 1
# four = 2 + 2
# for i in 1..100
# i += 1
# Come up with three different ways to do it!
# There are no tests (yet) for this.

def solution_one
  x = 'helloworld'.length
  ((x / x)..(x * x)).each do |i|
    puts i
  end
end

def solution_two
  array = ['Hello', 'World']
  ten = (array.index('World').to_s + array.index('Hello').to_s).to_i
  (ten * ten).times do |i|
    puts i + array.index('World')
  end
end

def solution_three
  one = 'world' <=> 'hello'
  zero = 'hello' <=> 'hello'
  ten = (one.to_s + zero.to_s).to_i
  i = one
  until i > ten * ten
    puts i
    i += one
  end
end

# solution_one
# solution_two
 # solution_three
