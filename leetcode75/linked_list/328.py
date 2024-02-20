class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head  # 연결 리스트가 비었거나 한 노드만 있는 경우

        odd = head  # 홀수 인덱스 노드 처리를 위한 포인터
        even = head.next  # 짝수 인덱스 노드 처리를 위한 포인터
        evenStart = head.next  # 짝수 인덱스 노드의 시작점

        while even and even.next:
            # 홀수 노드를 다음 홀수 인덱스 노드로 연결
            odd.next = even.next
            odd = odd.next
            # 짝수 노드를 다음 짝수 인덱스 노드로 연결
            even.next = odd.next
            even = even.next

        # 홀수 노드의 끝과 짝수 노드의 시작을 연결
        odd.next = evenStart

        return head
