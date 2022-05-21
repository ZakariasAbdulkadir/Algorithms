class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSums(root):
    return branchSumsHelper(root, [], 0)

def branchSumsHelper(node, array, sum):
    sum += node.value
    if node == None:
        return 
    if node.left == None and node.right == None:
        array.append(sum)
        return
    
    branchSumsHelper(node.left, array, sum)
    branchSumsHelper(node.right, array, sum)
    return array

x = BinaryTree(5)
x.left = BinaryTree(4)
x.right = BinaryTree(3)
print(branchSums(x))