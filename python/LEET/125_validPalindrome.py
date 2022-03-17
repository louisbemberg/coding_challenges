import re

class Solution:
    # bad approach, as it traverses the entire string
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    
    # Theoretically faster, but slower on leet (?)
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r"(\W|_)", "", s).lower()
        left, right = 0, len(s) - 1

        while left < right:
            
            if s[left] != s[right]: 
                return False
            left += 1
            right -= 1

        return True

    # Optimal solution, including building own ASCII check.
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1

        while left < right:
            while not alphaNum(s[left]) and left<right:
                left += 1
            while not alphaNum(s[right]) and right>left:
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
        
        return True
    
    def alphaNum(self, c):
        ascii = ord(c)
        return  (ord('A') <= ascii <= ord('Z') or
                ord('a') <= ascii <= ord('z') or
                ord('0') <= ascii <= ord('9'))