# O(n) time, O(log(n))/O(d) space
def maxPathSum(tree):
    _, maxPath = findMaxPathSum(tree)
    return maxPath

def findMaxPathSum(tree):
    if tree is None:
        return (0,0)
    
    branchLeft, contendorLeft = findMaxPathSum(tree.left)
    branchRight, contendorRight = findMaxPathSum(tree.right)
    largerBranch = max(branchLeft, branchRight)

    currentNode = tree.value
    currentBranch = max(largerBranch + currentNode, currentNode)
    createContendor = max(currentBranch, branchLeft + currentNode + branchRight)
    winningContendor = max(createContendor, contendorLeft, contendorRight)
    
    return (currentBranch, winningContendor)
