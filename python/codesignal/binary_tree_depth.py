# https://www.youtube.com/watch?v=hTM3phVI6YQ


# coding the largest depth of a tree, several different ways
# depth = path from the root to a leaf node.
# note that length = # of nodes


# Recursive DFS!
def depth_recursive(root):
    # checking if the tree is null
    if not root: return 0
    
    # recursive call.
    # 
    return 1 + max(depth_recursive(root.left), depth_recursive(root.right))


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
#    3
#  9   20
# - - 15 7

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
        