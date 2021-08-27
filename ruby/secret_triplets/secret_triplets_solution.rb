# There is a secret string which is unknown to you. Given a collection of random triplets from the string, recover the original string.
# A triplet here is defined as a sequence of three letters such that each letter occurs somewhere before the next in the given string. "whi" is a triplet for the string "whatisup".
# As a simplification, you may assume that no letter occurs more than once in the secret string.
# You can assume nothing about the triplets given to you other than that they are valid triplets and that they contain sufficient information to deduce the original string. In particular, this means that the secret string will never contain letters that do not occur in one of the triplets given to you.

def secret_word(triplets)
  chars = triplets.flatten.uniq
  triplets.each do |triplet|
    # if triplet0 is to the right of triplet1
    if chars.index(triplet[0]) > chars.index(triplet[1])
      chars.insert(chars.index(triplet[1]), chars.delete_at(chars.index(triplet[0]))) # we move trip0 to the left of trip1
    end
    # if triplet0 is to the right of triplet2
    if chars.index(triplet[0]) > chars.index(triplet[2])
      chars.insert(chars.index(triplet[2]), chars.delete_at(chars.index(triplet[0]))) # we move trip0 to the left of trip1
    end
    # if triplet1 is to the right of triplet2
    if chars.index(triplet[1]) > chars.index(triplet[2])
      chars.insert(chars.index(triplet[2]), chars.delete_at(chars.index(triplet[1]))) # we move trip1 to the left of trip2
    end
  end
  chars.join
end

secret1 = 'whatisup'
triplets1 = [
  ['t', 'u', 'p'],
  ['w', 'h', 'i'],
  ['t', 's', 'u'],
  ['a', 't', 's'],
  ['h', 'a', 'p'],
  ['t', 'i', 's'],
  ['w', 'h', 's']
]

p secret_word(triplets1) # =>  "whatisup"
puts '✅' if secret_word(triplets1) == secret1

# ALGORITHM LOGIC
# row 0
# swhtaupi # we start off with a random order of the unique letters:

# row 1
# swhtaupi # t to the left of u, t to the left of p
# swhtaupi # u to the left of p

# row 2
# swhtaupi # w to the left of h, w to the left of i
# swhtaupi # h to the left of i

# row 3
# tswhaupi # t NOT to the left of s, we move. t to the left of u
# tswhaupi # s to the left of u

# row 4
# atswhupi # a NOT to the left of t, we move. a to the left of s
# atswhupi # t to the left of s

# row 5
# hatswupi # h NOT to the left of a, we move. h to the left of p.
# hatswupi # a to the left of p.

# row 6
# hatswupi # t to the left of i, t to the left of s.
# hatiswup # i NOT to the left of s, we move.

# row 7
# whatisup # w NOT to the left of h, we move. w to the left of s.
# whatisup # h to the left of s.
