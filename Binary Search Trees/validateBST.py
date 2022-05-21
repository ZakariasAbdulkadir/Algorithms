# O(n) time | O(d) space
def validateBST(tree):
    return validateBstHelper(tree, float("-inf"), float("inf"))

def validateBstHelper(tree, min, max):
    if tree is None:
        return True
    elif tree < min or tree >= max:
        return False
    validateLeft = validateBstHelper(tree.left, min, tree.value)
    return validateLeft and validateBstHelper(tree.right, tree.value, max)