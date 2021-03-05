# A panagram is a sentence that contains every single letter of the alphabet at least once.
# Example: "The quick brown fox jumps over the lazy dog"
# Build a method that checks for pangrams.
# Return true if it is, false if not.
# Must be case insensitive, and ignore space and punctuation.

# Solution 1: using GSub & Regex
def panagram?(string)
  return false if string.length < 26

  letters = string.downcase.gsub(/[^a-z]/, '')
  letters.chars.uniq.count >= 26
end

# Solution 2: alphabet range
def panagram2?(string)
  ('a'..'z').all? { |letter| string.downcase.include?(letter) }
end

# Solution 3: Making use of regex scan to simplify solution 1
def panagram3?(string)
  string.downcase.scan(/[a-z]/).uniq.size == 26
end

# TESTS - run the file to get feedback :)
puts "Expected: false Got: #{panagram?('Hello World')}"
puts "Expected: false Got: #{panagram?('')}"
puts "Expected: true Got: #{panagram?('a_ab^^b0c56cddeeff_g, ghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz')}"
puts "Expected: true Got: #{panagram?('The quick brown fox jumps over the lazy dog')}"
puts "Expected: true Got: #{panagram?('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z')}"
