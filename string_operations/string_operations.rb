# When you first started to learn ruby, you were introduced to methods such as:
# "hello".upcase => "HELLO"
# "hello".capitalize => "Hello"
# "HELLO".downcase => "hello"
# "hello".gsub("l", "y") => "heyyo"
# "     hello       ".strip => "hello"

# Today, we're going to build these methods from scratch!
# Rules:
# you are not allowed to use the original methods to solve the problem.
# the methods need to behave the same way. upcase("hello") != "hello".upcase
# remember, methods without ! are non destructive.
# let's also build a my_upcase! destructive method to see the difference.
# For simplicity, you may ignore special letter such as é, è, ø, etc.
# You're given a DICTIONARY constant - feel free to print it out.
DICTIONARY = Hash[('a'..'z').zip('A'..'Z')]

# build a "my_upcase" method below!

# build a "my_capitalize" method below!

# build a "my_downcase" method below!

# build a "my_gsub" method below!

# build a "my_strip" method below!

# build a "my_upcase!" method below!

# TESTS - RUN THE FILE TO GET FEEDBACK!
puts 'TEST 1 - my_upcase'
string1 = 'hello'
puts string1.my_upcase == 'HELLO' ? 'test passed ✅' : 'test failed ❌'
puts string1 == 'HELLO' ? 'test failed ❌' : 'test passed ✅'
puts
puts 'TEST 2 - my_capitalize'
string2 = 'hello'
puts string2.my_capitalize == 'Hello' ? 'test passed ✅' : 'test failed ❌'
puts string2 == 'Hello' ? 'test failed ❌' : 'test passed ✅'
puts
puts 'TEST 3 - my_downcase'
string3 = 'HELLO'
puts string3.my_downcase == 'hello' ? 'test passed ✅' : 'test failed ❌'
puts string3 == 'hello' ? 'test failed ❌' : 'test passed ✅'
puts
puts 'TEST 4 - my_gsub'
string4 = 'HELLO'
p string4.my_gsub('L', '7')
puts string4.my_gsub('L', '7') == 'HE77O' ? 'test passed ✅' : 'test failed ❌'
puts string4 == 'HE770' ? 'test failed ❌' : 'test passed ✅'
puts
puts 'TEST 5 - my_strip'
string5 = '        H E L L O        '
p string5.my_strip
puts string5.my_strip == 'H E L L O' ? 'test passed ✅' : 'test failed ❌'
puts string5 == 'H E L L O' ? 'test failed ❌' : 'test passed ✅'
puts
puts 'TEST 6 - my_upcase!'
string6 = 'hello'
p string6.my_upcase!
puts string6.my_upcase! == 'HELLO' ? 'test passed ✅' : 'test failed ❌'
puts string6 == 'HELLO' ? 'test passed ✅' : 'test failed ❌'
