# # O(n) time | O(n)
# def flattenBinaryTree(root):
#     inOrder = flattenTree(root, [])
#     for i in range(0, len(inOrder) - 1):
#         left = inOrder[i]
#         right = inOrder[i+1]
#         left.right = right
#         right.left = left
#     return inOrder[0]


# def flattenTree(node, array):
#     if node is not None:
#         flattenTree(node.left, array)
#         array.append(node)
#         flattenTree(node.right, array)
#     return array

# O(n) time | O(log(n)) time
def flattenBinaryTree(root):
    leftMost, _ = flattenTree(root)
    return leftMost
def flattenTree(node):
    if node.left is None:
        leftMost = node
    else:
        ltLeftMost, ltRightMost = flattenTree(node.left)
        connectNodes(ltRightMost, node)
        leftMost = ltLeftMost
    
    if node.right is None:
        rightMost = node
    else:
        rtLeftMost, rtRightMost = flattenTree(node.right)
        connectNodes(node, rtLeftMost)
        rightMost = rtRightMost

    return (leftMost, rightMost)

def connectNodes(left, right):
    left.right = right
    right.left = left
        