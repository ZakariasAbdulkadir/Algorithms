def removeNthNodeFromEnd(head, n):
    counter = 1
    first = head
    second = head
    while counter <= n:
        second = second.next
        counter += 1
    if second is None:
        head = first.next
        return
    while second.next is not None:
        second = second.next
        first =  first.next
    first.next = first.next.next
    return head

# O(n) time | O(1) space
# Two pointers where S moves n nodes in front of F then they move together until S
# reaches the end and F is the node we remove