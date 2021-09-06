# Bob is preparing to pass IQ test. The most frequent task in this test is to find out which one of the given numbers differs from the others. Bob observed that one number usually differs from the others in evenness. Help Bob — to check his answers, he needs a program that among the given numbers finds one that is different in evenness, and return a position of this number.
# ! Keep in mind that your task is to help Bob solve a real IQ test, which means indexes of the elements start from 1 (not 0)
# https://www.codewars.com/kata/552c028c030765286c00007d/train/python
# once the number is identified, return its index (starting from)


# slightly longer solution that is optimal for minmal amount of loops
def iq_test(numbers):
    # 0 for even, 1 for odd
    counter = {0: 0, 1: 0}
    numbers_list = numbers.split()
    for idx, n in enumerate(numbers_list):
        counter[0 if int(n) % 2 == 0 else 1] += 1
        # current_min tracks whether even (0) or odd (1) has the least amount of counts
        current_min = min(counter, key=counter.get)
        if idx >= 2 and (counter[current_min] == 1):
            for idy, i in enumerate(numbers_list[idx - 2 : idx + 1]):
                if int(i) % 2 == current_min:
                    correct_number = i
                    # since we looked in the list of the last 3, the real index is offset by that position of that sub array of 3
                    correct_index = idx - (2 - idy)
                    return correct_index +  1


# cleaner, but less optimal solution:

def iq_test(numbers):
    # convert numbers into a list of 1's (odd) and 0's (even)
    even_or_odd = [int(n)%2 for n in numbers.split()]
    # we count how many 0's. if more than one, we return the index of the  odd. if not, return the index of the even.
    return even_or_odd.index(1 if even_or_odd.count(0) > 1 else 0) + 1


print(iq_test("2 4 7 8 10")) # 7
print(iq_test("1 2 2")) # 1
print(iq_test('1 3 5 8 7 9 11')) # 8

# turn string into array of ints
# iterate over ints and count even / odds
# stop counting when you reached values of 1 & <= 2
# retrieve the number that has 1