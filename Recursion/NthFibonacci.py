# Question: Take in integer n and return nth fibonacci
# Hint: Cache fibonacci to reuse recursively / Iterate until n calcuate fibonacci iteratively 

# Tail Recursion
def fibonacci(n):
    return go(n, [0, 1])

def go(n, lastTwo):
    if n == 1:
        return lastTwo[0]
    if n == 2:
        return lastTwo[1]
    else:
        return go(n-1, [lastTwo[1], lastTwo[0] + lastTwo[1]]) 
    # go(5, [0,1]) / go(4, [1, 1]) / go(3, [1, 2]) / go(2, [2, 3]) 3 is returned
    
# O(n) time | O(1) space
def fibonacci(n):
    lastTwo = [0, 1]
    counter = 3
    while counter <= n:
        nextFib = lastTwo[0] + lastTwo[1]
        lastTwo[0] = lastTwo[1]
        lastTwo[1] = nextFib
        counter += 1
    return lastTwo[1] if n > 1 else lastTwo[0]

# O(n) time | O(n) space
def fibonacci(n, memoize = {1: 0, 2: 1}):
    if memoize[n]:
        return memoize[n]
    else:
        memoize[n] = fibonacci(n-1, memoize) + fibonacci(n-2, memoize)
        return memoize[n]



# O(2^n) time | O(n) space
def fibonacci(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)