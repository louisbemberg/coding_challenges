# bad approach: only counts the matchin parentheses
# fails to False this example: "(])["
class Solution:
    def isValid(self, s: str) -> bool:
        # approach: count the number of opening and closing:

        counts = {}
        for i in "()[]{}":
            counts[i] = 0

        for char in  s:
            counts[char] += 1 
        
        if not (counts['('] == counts[')'] and counts['['] == counts[']'] and counts['{'] == counts['}']):
            return False

# better approach: everytime you open something going from the left,
# you need to make sure that you close in the same order.
# => Use a stack!!!
# Whenever a closer appears, it needs to match what's at the top of the stack
class Solution:
    def isValid(self, s: str) -> bool:
        # reference for us to more quickly check if it's a match
        matches = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        open_stack = []

        for char in s:
            # if the character is an opening char
            if char not in matches:
                open_stack.append(char)
            # if a closing char
            else:
                if open_stack and open_stack[-1] == matches[char]:
                    open_stack.pop()
                else:
                    return False
        
        # at the end of the traversal, stack must be empty
        # aka, every opening must have found its match.
        # If not, return False. 
        return True if not open_stack else False