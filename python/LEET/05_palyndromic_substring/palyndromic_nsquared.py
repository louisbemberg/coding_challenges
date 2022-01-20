def longestPalindrome(s):
    best = s[0] # worst case we'll take the first char as palindrome
    max_length = 1
    for i in range(len(s)):
        # for odd palindromes
        left, right = i, i
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > max_length:
                best = s[left:right+1]
                max_length = right - left + 1
            left -= 1
            right += 1
        
        # for even palindromes
        left, right = i, i + 1
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if (right - left + 1) > max_length:
                best = s[left:right+1]
                max_length = right - left + 1
            left -= 1
            right += 1
    return best

print(longestPalindrome('ABCDEFGHIJKLMNOPQRSTUVWXYZ')) # A or Z
print(longestPalindrome("ABBA")) # ABBA
print(longestPalindrome("cbbd")) # bb
print(longestPalindrome("bb")) # bb
print(longestPalindrome("OcaracA")) # carac
print(longestPalindrome("a")) # a
print(longestPalindrome("babad")) # both  bab and aba are valid
print(longestPalindrome("ycaracaracx")) # caracarac
print(longestPalindrome("babad")) # bab or aba
print(longestPalindrome("abb")) # 
