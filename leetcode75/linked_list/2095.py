class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        # 리스트가 비었거나 한 개의 노드만 있는 경우
        if not head or not head.next:
            return None
        
        # 리스트 크기 계산
        size = 0
        current = head
        while current:
            size += 1
            current = current.next
        
        # 중간 노드의 인덱스 계산 (0-based indexing)
        mid = size // 2
        
        # 중간 노드 삭제
        current = head
        for _ in range(mid - 1):  # 중간 노드의 이전 노드까지 이동
            current = current.next
        current.next = current.next.next  # 중간 노드 삭제
        
        return head
