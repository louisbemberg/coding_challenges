# inspired from Codewars's "Is my friend cheating"
# A friend of mine takes the sequence of all numbers from 1 to n (where n > 0).
# Within that sequence, he chooses two numbers, a and b.
# He says that the product of a and b should be equal to the sum of all numbers in the sequence, excluding a and b.
# Given a number n, could you tell me the numbers he excluded from the sequence?

# n is assumed to be > 0. can be very large.
# TODO: find a pair a and b that satisfy the rules. return them as [[a, b], [b, a]].
# There may be a chance that the result is
# [[a, b], [b, a], [c, d], [d, c]]
# Return an empty array if no pairs were found.
def find_pair(n)
  solutions = []
  sum = (1 + n) * n.fdiv(2)
  (1..n).each do |a|
    # b = ((n**2) + n - 2 * a).fdiv(2 * (a + 2))
    b = (sum - a).fdiv(a + 1)
    solutions << [a, b.to_i] if (b % 1).zero? && b.between?(1, n)
  end
  solutions
end
