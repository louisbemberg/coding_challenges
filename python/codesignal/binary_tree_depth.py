# https://www.youtube.com/watch?v=hTM3phVI6YQ
# coding the largest depth of a tree, several different ways
# depth = path from the root to a leaf node.
# note that length = # of nodes
# Recursive DFS!

class Node:
   def __init__(self, value):
      self.left = None
      self.right = None
      self.value = value


def depth_recursive(root, loops=0):
    # checking if the tree is null
    print("\n depth_recursive was called")
    loops += 1
    if not root: 
        print("Leaf node reached.")
        return 0
    
    print("Current root is", root.value, "BEFORE LEFT RECURSIVE CALL")
    left = depth_recursive(root.left, loops)
    print("Current root is", root.value, "AFTER LEFT RECURSIVE CALL, BEFORE RIGHT")
    right = depth_recursive(root.right, loops)
    print("Current root is", root.value,"AFTER RIGHT RECURSIVE CALL, BEFORE FINAL RETURN", right)

    print("loops:", loops)
    return 1 + max(left, right)

#                10(#1)
#      20(#2)                   30(#7)
#   21(#3)     22(#6)        40(#8)      50(#9)
# 211(#4) 212(#5)                      60(#10) 70(#11)

ten = Node(10) 
twenty = Node(20)
twenty_one = Node(21)
twenty_two = Node(22)
two_one_one = Node(211)
two_one_two = Node(212)
thirty = Node(30)
fourty = Node(40)
fifty = Node(50)
sixty = Node(60)
seventy = Node(70)

ten.left = twenty
twenty.left = twenty_one
twenty.right = twenty_two
twenty_one.left = two_one_one
twenty_one.right = two_one_two
ten.right = thirty
thirty.left = fourty
thirty.right = fifty
fifty.left = sixty
fifty.right = seventy

depth_recursive(ten)

# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------




# without recursion: Iterative BFS
# intuitive approach: counting the amount of levels
def depth_iterative_bfs(root):
    if not root: return 0

    level = 1
    # faster than list for popping and appending. stands fore double-ended queue
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level

# Iterative DFS + pre-order
# keeping track of the depth of each tree


# Stack ordering logic: always left before right
# STACK
# NODE DEPTH
# 3    1
# 9    2
# 20   2
# 15   3
# 7    3

def depth_iterative_dfs(root):
    if not root: return 0

    stack = [[root, 1]]
    result = 1

    while stack:
        node, depth = stack.pop()

        if node:
            result = max(result, depth)
            stack.append([node.left, depth+1])
            stack.append([node.right, depth+1])
    return result




