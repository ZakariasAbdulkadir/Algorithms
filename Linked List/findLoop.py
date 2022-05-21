def findLoop(head):
    first = head.next
    second = head.next.next
    while first != second:
        first = first.next
        second = second.next.next
    first = head
    while first != second:
        first = first.next
        second = second.next
    return first
# O(n) time | O(1) space
# First moves 1 and second moves 2 until they overlap then first moves to head. They both move 1 
# at a time unitl they overlap at the start of the loop

