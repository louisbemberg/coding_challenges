# TODO: Build a method that checks for anagrams
# fyi: anagrams are words that have the same letters reordered
# ex: Elbow & Below, Stressed & Desserts, etc.
# the method receives 2 parameters: 1 word, and an array of words to check.
# ex: anagram_finder("Elbow", ["Hello, Bowel, Below"]) returns ["Bowel, Below"]
# the method returns and empty array if no anagrams found.

def anagrams(word, words)
  # TODO: check if "words" has anagrams of "word" and return them in an array
end

# TESTS - run the file to get feedback :)
puts "got: #{anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])} expected: ['aabb', 'bbaa']"
puts "got: #{anagrams('Hola', ['Halo', 'Hello', 'Bonjour'])} expected: ['Halo']"
puts "got: #{anagrams('Mango', ['Pear', 'Apple'])} expected: []"
