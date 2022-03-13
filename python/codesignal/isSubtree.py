# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None

def identical_trees(t1, t2):
    
    # both empty
    if not t1 and not t2:
        return True
    
    # both not empty
    if t1 and t2:
        return (t1.value == t2.value and identical_trees(t1.left, t2.left) and identical_trees(t1.right, t2.right))
    
    # if one is empty and the other isn't, must be false
    return False


def solution(t1, t2):
    
    # edge cases:
    if not t1 and not t2:
        return True
    elif not t2: 
        return True
    elif not t1:
        return False
    
    # if the current two trees are identical
    if identical_trees(t1, t2):
        return True
       
    # recursively check if the left child or right child is identical to t2 
    return (identical_trees(t1.left, t2) or identical_trees(t1.right, t2))
    
    
    
    # strategy:
    # build a helper function able to tell whether trees are identical

    # traverse t1 and do a subtree check everytime the starting nodes match.