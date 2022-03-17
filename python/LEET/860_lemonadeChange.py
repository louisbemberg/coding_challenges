class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = {
            5: 0,
            10: 0,
            20: 0
        }

        for bill in bills:
            # the customer pays, we get a bill
            bank[bill] += 1

            # if they gave a 5 we do nothing
            # (we just cash in the 5 on line 11)

            # if they gave a 10 we give a 5 back
            if bill == 10:
                if bank[5] >= 1:
                    bank[5] -= 1
                else:
                    return False
            # if they give a 20 we prefer to give back 10+5
            # if not possible we give 5+5+5
            # if not possible then we can't pay back
            elif bill == 20:
                if bank[5] >= 1 and bank[10] >= 1:
                    bank[5] -= 1
                    bank[10] -= 1
                elif bank[5] >= 3:
                    bank[5] -= 3
                else:
                    return False
       
        # If we reach the end of the loop we managed to pay back everyone
        return True

# Time Complexity: O(n), one  traversal of arrays + constant lookup times of map
# Space Complexity: O(1), we just store an array with 3 keys