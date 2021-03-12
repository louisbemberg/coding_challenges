# Every language has its own types of comments
# Ruby comments start with hashtags
# Other languages use <!--, !, //, etc.
# Write a method that gets rid of all comments of a string
# The method receives 2 arguments:
# 1) a string
# 2) an array containing the comment markers to check for
# example: comments("puts 'Hello World' # this is my fist line of code", ["#"])

def comments(string, markers)
end

# TESTS - Run the file to get feedback :)
puts
puts "TEST 1 - Ruby comments"
puts "result: #{comments('pi = 3.14 # declaring a variable', ['#'])} expected: pi = 3.14 "
puts
puts "TEST 2 - JS comments: "
puts "result: #{comments('const pi = 3.14 // declaring a variable', ['//'])} expected: const pi = 3.14"
puts
puts "TEST 3 - JS and Ruby comments on different lines:"
puts "result:"
puts comments("const pi = 3.14 // declaring a variable\npi = 3.1415 #declaring a variable in ruby", ['//', '#'])
puts "expected:"
puts "pi = 3.14\npi = 3.1415"
puts
puts "TEST 4 - No comments, no line jumps: "
puts "result: #{comments('const pi = 3.14', ['//', '#'])} expected: const pi = 3.14"
puts
puts "TEST 5 - No comments, line jumps: "
puts "result:"
puts comments("const pi = 3.14\nconst e = mc^2", ['//', '#'])
puts "expected:"
puts "const pi =3.14\nconst e = mc^2"
puts
puts "TEST 6 - Identical Text before and after"
puts "result: #{comments("HelloWorld#HelloWorld", ['#'])} expected: HelloWorld"
