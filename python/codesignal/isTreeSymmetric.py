#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None


def solution(t):
    # if there is no tree at all is it false or true? tbd...
    if not t: return True
    
    # if the tree only has 1 node it's symmetric
    if not t.left and not t.right: return True
    
    # call our helper function to check all the remaining subtrees
    return compare_children(t.left, t.right)
        

# function accepts a node from the left and a node from the right 
# who must be symmetrics themselves and whose children (LL-RR and LR - RL) must be symmetric
def compare_children(tree1, tree2):
    # If either one is null
    if not tree1 or not tree2:
        # return true if the other is null, otherwise return false
        return tree1 == tree2
    
    # if both values don't match, then return false
    if tree1.value != tree2.value:
        return False
    
    # Checking LL-RR and LR-RL crawling all the way down the tree
    # key idea: each set of "triangle" must be symmetric to one another
    return compare_children(tree1.left, tree2.right) and compare_children(tree1.right, tree2.left) 