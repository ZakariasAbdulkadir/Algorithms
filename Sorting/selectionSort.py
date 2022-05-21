# # O(n^2) time | O(1) space
# def selectionSort(array):
#     for i in range(len(array)):
#         min = i
#         for j in range(i+1, len(array)):
#             if array[j] < array[min]:
#                 min = j
        
#         if min != i:
#             swap(i, min, array)
    
#     return array
    
def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

# Find the min and swap the first from the unsorted section with the min
def selectionSort(array):
    currentIdx = 0
    while currentIdx < len(array):
        smallestIdx = currentIdx
        for i in range(currentIdx + 1, len(array)):
            if array[smallestIdx] > array[i]:
                smallestIdx = i
        swap(currentIdx, smallestIdx, array)
        currentIdx += 1
    
    return array


            

