# this solution works but exceeds the time limit
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        right = k - 1
        largest_avg = -100000

        while right < len(nums):
            avg = sum(nums[left:right+1])/k
            if avg > largest_avg:
                largest_avg = avg

            left += 1
            right += 1
        
        return largest_avg


# better approach:
    class Solution:
        def findMaxAverage(self, nums: List[int], k: int) -> float:
            # logic:
            # the difference between the previous average and the new one
            # is removing the first number and adding the latest, no need to recompute everything
            
            # pointers for sliding window
            left = 0
            right = k - 1
            # logic for the if statement below
            average = None
            # works because we're told that none of the numbers are smaller than that
            biggest_average = -100000

            while right < len(nums):
                if average:
                    average = average - nums[left-1]/k + nums[right]/k
                else:
                    average = sum(nums[left:right+1])/k

                if biggest_average < average:
                    biggest_average = average

                left += 1
                right += 1

            return biggest_average

            # further improvement: avoid dividing about the very end.
            # you only care about the division for the return. 

            # other further improvement: no need for left,right, as k helps you find them.
            