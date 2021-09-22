# https://leetcode.com/problems/longest-palindromic-substring/

# brute force: it works but it's slow AF ( O(n^3) )
def longestPalindrome(s):
    # code here
    i, j, n = 0, 0, len(s)
    palindromes = []
    if n == 1:
        palindromes.append(s)
    else:
        for i in range(0,len(s)):
            for j in range(0, len(s)):
                if palindrome(s[i:j+1]) and s[i:j+1] != '':
                    palindromes.append(s[i:j+1])
        print(max(palindromes, key=len))

def palindrome(string):
    return string.lower() == string[::-1].lower()



palindrome('hello') # False
palindrome('hahah') # True

longestPalindrome('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
longestPalindrome("ABBA") # ABBA
longestPalindrome("cbbd") # bb
longestPalindrome("bb") # bb
longestPalindrome("OcaracA") # carac
longestPalindrome("a") # a
longestPalindrome("babad") # both  bab and aba are valid
longestPalindrome("ycaracaracx") # caracarac
