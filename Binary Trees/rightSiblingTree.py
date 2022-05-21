# O(n) time | O(1) space
def rightSiblingTree(root):
    mutate(root, None, None)
    return root

def mutate(node, parent, isLeftChild):
    if node is None:
        return
    left, right = node.left, node.right
    mutate(node.left, node, True)
    if isLeftChild:
        node.right = parent.right
    elif parent is None:
        node.right = None
    else:
        if parent.right is None:
            node.right == None
        else:
            node.right = parent.right.left
    mutate(node.right, node, False)

