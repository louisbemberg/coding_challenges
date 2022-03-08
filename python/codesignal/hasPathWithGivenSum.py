# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

# using a helper dfs function
def solution2(t, s):
    return dfs(t, 0, s)


def dfs(node, current_sum, target_sum):
    if not node: return False
    
    current_sum += node.value
    
    if not node.left and not node.right:
        return current_sum == target_sum
    
    return dfs(node.left, current_sum, target_sum) or dfs(node.right, current_sum, target_sum)


# other way to solve it
def solution(t, s):
    # return false if tree is null
    if not t: return False
    
    # Checking if we're at the leaf. If so, did we reach the desired sum?
    if not t.left and not t.right:
        return s - t.value == 0
    
    # move to the next node and reduce s until it reaches 0 (or not!)
    # note that 
    return solution(t.left, s - t.value) or solution(t.right, s - t.value)



# even simpler
def solution(t, s):
    if t is None:
        return s == 0    

    return solution(t.left, s - t.value) or solution(t.right, s - t.value)