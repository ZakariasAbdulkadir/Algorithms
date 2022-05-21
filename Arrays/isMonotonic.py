# # O(n) time | O(1) space
# def isMonotonic(array):
#     if len(array) <= 2:
#         return True

#     direction = array[1] - array[0]
#     for i in range(2, len(array)):
#         if direction == 0:
#             direction = array[i] - array[i-1]
#             continue
#         if breaksDirection(direction, array[i-1], array[i]):
#             return False

#     return True

# def breaksDirection(direction, left, right):
#     difference = right - left
#     if direction < 0:
#         return difference > 0
#     return difference < 0

# O(n) time | O(1) space
def isMonotonic(array):
    isNonIncreasing = True
    isNonDecreasing = True
    for i in range(1, len(array)):
        if array[i] > array[i-1]:
            isNonIncreasing = False
        if array[i] < array[i-1]:
            isNonDecreasing = False

    return isNonDecreasing and isNonIncreasing


