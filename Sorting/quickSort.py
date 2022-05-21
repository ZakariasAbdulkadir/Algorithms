# Pick a pivot - smaller number on the left and larger numbers on the right
# Repeat with left/right subarrays
# Worst Case - O(nLog(n)) time | O(log(n))
# O(n) loop log(n) times
def quickSort(array):
    quickSortHelper(array, 0, len(array) - 1)
    return array

def quickSortHelper(array, startIdx, endIdx):
    if endIdx <= startIdx:
        return
    pivotIdx = startIdx
    leftIdx = startIdx + 1
    rightIdx = endIdx
    while rightIdx >= leftIdx:
        if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
            swap(leftIdx, rightIdx, array)
        if array[leftIdx] <= array[pivotIdx]:
            leftIdx += 1
        if array[rightIdx] >= array[pivotIdx]:
            rightIdx -= 1
    swap(rightIdx, pivotIdx, array)
    isLeftSubarraySmaller = (rightIdx - 1) - startIdx < endIdx - (rightIdx + 1)
    if isLeftSubarraySmaller:
        quickSortHelper(array, startIdx, rightIdx - 1)
        quickSortHelper(array, rightIdx + 1, endIdx)
    else:
        quickSortHelper(array, rightIdx + 1, endIdx)
        quickSortHelper(array, startIdx, rightIdx - 1)
        

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]