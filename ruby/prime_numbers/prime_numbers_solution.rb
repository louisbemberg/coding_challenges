# TODO: Return true or false based on if the integer provided is prime.
# Note: input may vary from 1 to 2^32 - so time efficiency matters.
# You are not allowed to use Ruby's Prime module.

def prime?(integer)
  return false if integer < 2 || (integer.even? && integer != 2)

  n = Math.sqrt(integer).floor
  (2..n).none? { |x| (integer % x).zero? }
end

# TESTS - run the file to get some feedback :)
puts "Got: #{prime?(2)} Expected: true [2]"
puts "Got: #{prime?(3)} Expected: true [3]"
puts "Got: #{prime?(5)} Expected: true [5]"
puts "Got: #{prime?(7)} Expected: true [7]"
puts "Got: #{prime?(19)} Expected: true [19]"
puts "Got: #{prime?(1453)} Expected: true [1453]"
puts "Got: #{prime?(5233)} Expected: true [5233]"
puts "Got: #{prime?(9941)} Expected: true [9941]"

puts
puts

puts "Got: #{prime?(18)} Expected: false [18]"
puts "Got: #{prime?(-45)} Expected: false [-45]"
puts "Got: #{prime?(63)} Expected: false [63]"
puts "Got: #{prime?(0)} Expected: false [0]"
puts "Got: #{prime?(1)} Expected: false [1]"

# uncomment those lines if you want to test a HUGE prime :)
# puts "Got: #{prime?(1_002_569)} Expected: true [1002569]"
# puts "Got: #{prime?(1_002_571)} Expected: false [1002571]"
