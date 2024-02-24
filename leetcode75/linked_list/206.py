# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        current = head
        while current:
            next = current.next  # Save next node
            current.next = prev  # Reverse current node's pointer
            prev = current  # Move prev one step forward
            current = next  # Move current one step forward
        head = prev  # Update head to new first element
        return head
