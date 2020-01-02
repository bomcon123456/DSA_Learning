class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        mid_node = self.findMidNode(head)
        reverse_list = self.reverse(mid_node)
        runA = head
        runB = reverse_list
        while runB is not None:
            if runB.val != runA.val:
                return False
            runA = runA.next
            runB = runB.next
        return True
    
    def findMidNode(self, head):
        slow_ptr = head
        fast_ptr = head
        while fast_ptr.next is not None and fast_ptr.next.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        return slow_ptr.next
            
    def reverse(self, head):
        prev = head
        cur = head.next
        while cur is not None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        head.next = None
        return prev
