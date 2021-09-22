# https://leetcode.com/problems/longest-palindromic-substring/

# Dynamic programming approach
def longestPalindrome(s):
    n = len(s)

    # create a n x n dynamic programming table (or matrix):
    table = [[0 for x in range(n)] for y in range(n)]
    
    # filling up the diagonal row: \. substrings of length 1 are palindromes 
    for i in range(0,n):
        table[i][i] = 1
    
    # filling up adjacent of diagonal row (palindrome of length 2)
    for i in range(0, n  - 1):
        if s[i] == s[i + 1]: # palindrome of size 2 check
            table[i][i+1] = 1

    # check for any bigger palindrome:
    size = 3
    while size <= n:
        i = 0
        while i < (n - size + 1):
            j = i + size - 1

            if table[i+1][j-1] and s[i] == s[j]:
                table[i][j] == 1
            i += 1
        size += 1


    print(table)

def palindrome(string):
    return string.lower() == string[::-1].lower()



palindrome('hello') # False
palindrome('hahah') # True

# longestPalindrome('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
longestPalindrome("ABBA") # ABBA
# longestPalindrome("cbbd") # bb
# longestPalindrome("bb") # bb
# longestPalindrome("OcaracA") # carac
# longestPalindrome("a") # a
# longestPalindrome("babad") # both  bab and aba are valid
# longestPalindrome("ycaracaracx") # caracarac
