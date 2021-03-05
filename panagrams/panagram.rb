# A panagram is a sentence that contains every single letter of the alphabet at least once.
# Example: "The quick brown fox jumps over the lazy dog"
# Build a method that checks for panagrams.
# Return true if it is, false if not.
# Must be case insensitive, and ignore space and punctuation.

def panagram?(string)
end

# TESTS - run the file to get feedback :)
puts "Expected: false Got: #{panagram?('Hello World')}"
puts "Expected: false Got: #{panagram?('')}"
puts "Expected: true Got: #{panagram?('a_ab^^b0c56cddeeff_g, ghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz')}"
puts "Expected: true Got: #{panagram?('The quick brown fox jumps over the lazy dog')}"
puts "Expected: true Got: #{panagram?('A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z')}"
