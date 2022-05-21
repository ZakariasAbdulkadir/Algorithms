# O(n) time: Traversing All Nodes
# O(n) space: Array Takes up Memory
# O(d) space: d = depth of tree if you printed insted of appending to an array
# The space of O(d) would be the frames on a call stack
def inOrderTraversal(tree, array):
    if tree is not None:
        inOrderTraversal(tree.left, array)
        array.append(tree.value)
        inOrderTraversal(tree.right, array)
    return array

def preOrderTraversal(tree, array):
    if tree is not None:
        array.append(tree.value)
        preOrderTraversal(tree.left, array)
        preOrderTraversal(tree.right, array)
    return array

def postOrderTraversal(tree, array):
    if tree is not None:
        postOrderTraversal(tree.left, array)
        postOrderTraversal(tree.right, array)
        array.append(tree.value)
    return array