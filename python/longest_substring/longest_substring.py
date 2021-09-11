# Given a string s, find the length of the longest substring without repeating characters.

# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# my solution: iterate once over the characters and keep track of duplicates in a second array.
# def longest_substring(s):
#     substrings = ''
#     lengths = [0]
#     for letter in s:
#         if letter in substrings:
#             lengths.append(len(substrings))
#             substrings = substrings[substrings.index(letter)+ 1:]
#             substrings.append(letter)
#         else:
#             substrings.append(letter)
#     return max(max(lengths), len(substrings))

# other approach, slightly more efficient
def longest_substring(s):
    if len(s) <= 1: return len(s)

    max_length = 0
    substring = ''
    for letter in s:
        if letter in substring:
            substring = substring[substring.index(letter)+1:]
        substring += letter
        if len(substring) > max_length: max_length = len(substring)
    return max_length




print(longest_substring("aaabc")) # 3
print(longest_substring("ABCDEFGA")) # 7
print(longest_substring("ABABCABCDABCDEF")) # 6
print(longest_substring("AAAAAAAABCDEFGHIAAAAA")) # 9
print(longest_substring("pwwkew")) # 3
print(longest_substring("dvdf")) # 3
print(longest_substring("")) # 0
print(longest_substring("abc")) # 3
print(longest_substring("aaa")) # 1



