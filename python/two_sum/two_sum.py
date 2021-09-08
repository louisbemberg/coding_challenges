import itertools

# complete bruteforce
def two_sum_bruteforce(nums, target):
    for index_i, i in enumerate(nums):
        for index_j, j in enumerate(nums):
           if i + j == target: return [index_i, index_j] 

# bruteforce but letting itertools doing the hard work
def two_sum_bruteforce_v2(nums, target):
    combs = list(itertools.combinations(nums, 2))
    for tup in combs:
        if sum(tup) == target: return [nums.index(i) for i in tup]

# more efficient


print(two_sum_bruteforce([2,7,11,15], 9)) # should be [0, 1] or [1, 0]

print(two_sum_bruteforce_v2([2,4,22,10,3,29], 7)) # should be [1, 4] or [4, 1]
