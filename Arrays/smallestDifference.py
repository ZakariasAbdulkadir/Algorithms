# O(n*log(n) + m*log(m)) time | O(1) space
def smallestDifference(arrayOne, arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()
    idxOne = 0
    idxTwo = 0
    smallest = float("inf")
    smallestPair = []
    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        left = arrayOne[idxOne]
        right = arrayTwo[idxTwo]
        current = abs(left - right)
        if left < right:
            idxOne += 1
        elif right < left:
            idxTwo += 1
        else:
            return [left, right]
        if current < smallest:
            smallest = current
            smallestPair = [left, right]    
    return smallestPair

