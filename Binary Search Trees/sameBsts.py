# Array method
#   O(n^2) time and O(n^2) space
def sameBsts(arrayOne, arrayTwo):
    if len(arrayOne) != len(arrayTwo):
        return False
    
    if arrayOne[0] != arrayTwo[0]:
        return False
    
    if len(arrayOne) == 0 and len(arrayTwo) == 0:
        return True
    
    smallerOne = getSmaller(arrayOne)
    smallerTwo = getSmaller(arrayTwo)
    biggerOne = getBigger(arrayOne)
    biggerTwo = getBigger(arrayTwo)

    return sameBsts(smallerOne, smallerTwo) and sameBsts(biggerOne, biggerTwo)

def getSmaller(array):
    smaller = []
    for i in range(1, len(array)):
        if array[i] < array[0]:
            smaller.append(array[i])
    return smaller

def getBigger(array):
    biggerOrEqual = []
    for i in range(1, len(array)):
        if array[i] >= array[0]:
            biggerOrEqual.append(array[i])
    return biggerOrEqual

# Itearate an array of length n to find values smaller and greater than the root at index 0. O(n) Loop
# Then iterate on the subtrees and their subtrees - An O(n) iteration n times leading to O(n^2) time

# Creating extra arrays for each subtree taking up space in memory leading to O(n^2) time complexity
# Without arrays the space is taken up by recursive calls on the call stack equal to the depth of the tree - O(d) space

def sameBst(arrayOne, arrayTwo):
    return sameBstHelper(arrayOne, arrayTwo, 0, 0, float("-inf"), float("inf"))

def sameBstHelper(arrayOne, arrayTwo, rootIdxOne, rootIdxTwo, minVal, maxVal):
    if rootIdxOne == -1 or rootIdxTwo == -1:
        return rootIdxOne == rootIdxTwo 
    
    if arrayOne[rootIdxOne] != arrayTwo[rootIdxTwo]:
        return False
    
    leftrootIdxOne = getIdxOfFirstSmaller(arrayOne, rootIdxOne, maxVal)
    leftrootIdxTwo = getIdxOfFirstSmaller(arrayTwo, rootIdxOne, maxVal)
    rightRootIdxOne = getIdxOfSecondBigger(arrayOne, rootIdxTwo, minVal)
    rightRootIdxTwo = getIdxOfSecondBigger(arrayTwo, rootIdxTwo, minVal)

    currentNode = arrayOne[leftrootIdxOne]
    leftTree = sameBstHelper(arrayOne, arrayTwo, leftrootIdxOne, leftrootIdxTwo, minVal, currentNode)
    rightTree = sameBstHelper(arrayOne, arrayTwo, leftrootIdxOne, leftrootIdxTwo, currentNode, maxVal)

    return leftTree and rightTree

def getIdxOfFirstSmaller(array, startingIdx, max):
    for i in range(startingIdx + 1, len(array)):
        if array[i] < array[startingIdx] and array[i] < max:
            return i
    return -1


def getIdxOfSecondBigger(array, startingIdx, min):
    for i in range(startingIdx + 1, len(array)):
        if array[i] >= array[startingIdx] and array[i] >= min:
            return i
    return -1

    