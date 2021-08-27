# Task: Given a range from :start to :end , and array of integers,
# count numbers that are divisible by the numbers in the array.

def divisible_numbers_simple(numbers_hash)
  amount_of_loops = 0
  count = 0
  (numbers_hash[:start]..numbers_hash[:end]).each do |n|
    amount_of_loops += 1
    count += 1 if numbers_hash[:arr].any? { |x|
      amount_of_loops += 1
      (n % x).zero? }
  end
  puts "#{amount_of_loops} loops"
  count
end

def divisible_numbers(numbers_hash)
  amount_of_loops = 0
  # save range in a variable
  range = (numbers_hash[:start]..numbers_hash[:end]).to_a
  # find the first multiple of each arr element in the range
  first_multiples = numbers_hash[:arr].map do |i|
    amount_of_loops += 1
    range.find { |j|
      amount_of_loops += 1
      j % i == 0 }
  end
  # add all the subsequent multiples in a new array that aren't bigger than end
  all_multiples = []
  first_multiples.each_with_index do |multiple, index|
    amount_of_loops += 1
    i = 0
    while multiple + numbers_hash[:arr][index] * i <= numbers_hash[:end]
      amount_of_loops += 1
      all_multiples << multiple + numbers_hash[:arr][index] * i
      i += 1
    end
  end
  puts "#{amount_of_loops} loops"
  all_multiples.uniq.size
end

test1 = {
  start: 10,
  end: 20,
  arr: [3, 5, 7]
}

test2 = {
  start: 10,
  end: 20_000,
  arr: [3, 6, 10, 14]
}

test3 = {
  start: 38361988,
  end: 773523136,
  arr: [85997, 303398, 962260, 552134, 590708, 4416]
}

puts "test input:"
p test2

start = Time.now
puts "Sam's Idea"
p divisible_numbers_simple(test3)
finish = Time.now
puts "Elapsed time: #{finish - start} seconds"

start = Time.now
puts "Louis's Idea"
p divisible_numbers(test3)
finish = Time.now
puts "Elapsed time: #{finish - start} seconds"
