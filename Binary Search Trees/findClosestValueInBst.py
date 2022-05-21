#Recursive
#   Average O(log(n)) time | O(log(n)) space
#   Worst O(n) time | O(n) space
def findClosestValue(tree, target):
    return findClosestValueHelper(tree, target, float("inf"))

def findClosestValueHelper(tree, target, closest):
    if tree is None:
        return closest
    if abs(target - closest) > abs(target - tree.value):
        closest = tree.value
    if closest < tree.target:
        findClosestValue(tree.right, target, closest)
    elif closest > tree.target:
        findClosestValue(tree.left, target, closest)
    else:
        return closest

#Iterative
#   Average O(log(n)) time | O(1) space
#   Worst O(n) time | O(1) space
def iterativeFindClosest(tree, target):
    closest = float("inf")
    currentNode = tree
    while currentNode is not None:
        if abs(target - closest) > abs(target - currentNode.value):
            closest = currentNode.value
        if currentNode.value < target:
            currentNode = currentNode.right
        elif currentNode.value > target:
            currentNode = currentNode.left
        else:
            break
    return closest