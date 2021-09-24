# https://leetcode.com/problems/longest-palindromic-substring/

# Dynamic programming approach
def longestPalindrome(s):
    n = len(s)
    max_pal_length = 1
    max_start = 0

    # create a n x n dynamic programming table (or matrix):
    table = [[0 for x in range(n)] for y in range(n)]
    
    # filling up the diagonal row: \. substrings of length 1 are palindromes 
    for i in range(0,n):
        table[i][i] = 1
    
    # filling up adjacent of diagonal row (palindrome of length 2)
    for i in range(0, n  - 1):
        if s[i] == s[i + 1]: # palindrome of size 2 check
            table[i][i+1] = 1
            max_pal_length = 2
            max_start = i

    # check for any bigger palindrome:
    size = 3
    while size <= n:
        i = 0
        while i < (n - size + 1):
            j = i + size - 1

            if table[i+1][j-1] == 1 and s[i] == s[j]:
                table[i][j] = 1
                if size > max_pal_length:
                    max_start = i
                    max_pal_length = size
            i += 1
        size += 1
    # print(table)
    print('your palindrome starts with', s[max_start], 'at index', max_start, 'and is', max_pal_length, 'long')
    return s[max_start:max_start + max_pal_length]

print(longestPalindrome('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) # A or Z
print(longestPalindrome("ABBA")) # ABBA
print(longestPalindrome("cbbd")) # bb
print(longestPalindrome("bb")) # bb
print(longestPalindrome("OcaracA")) # carac
print(longestPalindrome("a")) # a
print(longestPalindrome("babad")) # both  bab and aba are valid
print(longestPalindrome("ycaracaracx")) # caracarac
print(longestPalindrome("babad")) # bab or aba
