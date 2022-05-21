# # O(n^2) time | O(1) space
# def twoNumberSum(array, targetSum):
#     for i in range(len(array)):
#         for j in range(i+1, len(array) - 1):
#             if array[i] == array[j]:
#                 return [array[i], array[j]]
#     return []

# # O(n) time | O(n) space
# def twoNumbersSum(array, targetSum):
#     potentialMatch = {}
#     for num in array:
#         if potentialMatch[targetSum - num]:
#             return [num, targetSum - num]
#         else:
#             potentialMatch[num] = True
#     return []

# O(n*log(n)) time | O(1) space
def twoNumbersSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1
    while left < right:
        currentSum = array[left] + array[right]
        if currentSum == targetSum:
            return [left, right]
        elif currentSum < targetSum:
            left += 1
        elif currentSum > targetSum:
            right -= 1
    return []
