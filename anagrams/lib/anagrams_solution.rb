# TODO: Build a method that checks for anagrams
# fyi: anagrams are words that have the same letters reordered
# ex: Elbow & Below, Stressed & Desserts, etc.
# the method receives 2 parameters: 1 word, and an array of words to check.
# ex: anagram_finder("Elbow", ["Hello, Bowel, Below"]) returns ["Bowel, Below"]
# the method returns and empty array if no anagrams found.

# Initial version, using hash notation:
def anagrams(word, words)
  main_word_hash = letter_hash(word)
  words.select { |w| main_word_hash == letter_hash(w) }
end

def letter_hash(word)
  word_hash = {}
  word.chars.each do |c|
    word_hash[c] ? word_hash[c] += 1 : word_hash[c] = 1
  end
  word_hash
end

# Refactored solution
def better_anagrams(word, words)
  words.chars.select { |w| w.chars.sort == word.chars.sort }
end

# TESTS - run the file to get feedback :)
puts "got: #{anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada'])} expected: ['aabb', 'bbaa']"
puts "got: #{anagrams('Hola', ['Halo', 'Hello', 'Bonjour'])} expected: ['Halo']"
puts "got: #{anagrams('Mango', ['Pear', 'Apple'])} expected: []"
