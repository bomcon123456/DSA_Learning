class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def addTwoNumbers(l1, l2):
    l1_pointer = l1
    l2_pointer = l2
    carry = 0
    res = current = None
    while l1_pointer or l2_pointer:
        val = l1_pointer.val + l2_pointer.val + carry
        carry = val // 10
        val = val % 10
        if current is None:
            res = current = ListNode(val)
        else:
            current.next = ListNode(val)
            current = current.next
        if l1_pointer.next or l2_pointer.next:
            if l1_pointer.next == None:
                l1_pointer.next = ListNode(0)
            elif l2_pointer.next == None:
                l2_pointer.next = ListNode(0)
        l1_pointer = l1_pointer.next
        l2_pointer = l2_pointer.next
    if carry != 0:
        current.next = ListNode(carry)
    return res

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)


l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

res = addTwoNumbers(l1, l2)
while res is not None:
    print(res.val)
    res = res.next