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

# Test.assert_equals(removNb(26), [[15, 21], [21, 15]])
# Test.assert_equals(removNb(100), [])
# Test.assert_equals(removNb(101), [[55, 91], [91, 55]])
# Test.assert_equals(removNb(102), [[70, 73], [73, 70]])
# Test.assert_equals(removNb(110), [[70, 85], [85, 70]])
# Test.assert_equals(removNb(1006), [[546, 925], [925, 546]])
# Test.assert_equals(removNb(103), [])
# Test.assert_equals(removNb(446), [[252, 393], [393, 252]])
# Test.assert_equals(removNb(846), [[498, 717], [717, 498]])
# Test.assert_equals(removNb(1000003), [[550320, 908566], [559756, 893250], [893250, 559756], [908566, 550320]])
# Test.assert_equals(removNb(1000008), [[677076, 738480], [738480, 677076]])

# def removNbTest(n)
#     s = (n * (n +1) / 2)
#     res = []
#     i = (n / 2).to_i
#     while (i <= n) do
#         b = s - i
#         if (b % (i + 1) == 0) then
#             res << [i, b / (i + 1)]
#         end
#         i = i + 1
#     end
#     res
# end

# def randomTests()
#     someVals = [210, 211, 213, 220, 226, 231, 232, 249, 250, 257, 262,
#                 263, 265, 266, 282, 290, 297, 300, 304, 311, 312, 314,
#                 325, 340, 341, 346, 358, 362, 369, 378, 381, 386, 394
#                ]
#     x = 0
#     10.times do
#         rn = Random.rand(29)
#         f1 = someVals[rn]
#         puts("Random Tests ", x)
#         Test.assert_equals(removNb(f1), removNbTest(f1))
#         x += 1
#     end
# end

# randomTests()
