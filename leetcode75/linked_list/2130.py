# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        # Step 1: Find the midpoint of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Step 3: Calculate the twin sums and find the maximum
        max_sum = 0
        while prev:  # Now, prev is the head of the reversed second half
            max_sum = max(max_sum, head.val + prev.val)
            head = head.next
            prev = prev.next
        
        return max_sum
