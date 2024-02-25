class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        # 재귀 함수 종료 조건: 루트가 None이거나, p나 q 중 하나를 찾은 경우
        if root is None or root == p or root == q:
            return root
        
        # 왼쪽 서브트리에서 LCA 탐색
        left = self.lowestCommonAncestor(root.left, p, q)
        # 오른쪽 서브트리에서 LCA 탐색
        right = self.lowestCommonAncestor(root.right, p, q)
        
        # 만약 왼쪽과 오른쪽 서브트리에서 각각 p와 q를 찾았다면, 현재 노드가 LCA임
        if left and right:
            return root
        
        # p와 q 중 하나만 찾았다면, 찾은 노드를 반환
        return left if left else right
