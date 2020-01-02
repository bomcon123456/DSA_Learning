# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur_a = headA
        cur_b = headB
        length_a = 0
        while cur_a is not None:
            length_a+=1
            cur_a = cur_a.next
        length_b = 0
        while cur_b is not None:
            length_b+=1
            cur_b = cur_b.next    
        cur_a = headA
        cur_b = headB
        while length_a > length_b:
            cur_a = cur_a.next
            length_a -= 1
        while length_b > length_a:
            cur_b = cur_b.next
            length_b -= 1
        while cur_a != cur_b:
            cur_a = cur_a.next
            cur_b = cur_b.next
        return cur_a
        
