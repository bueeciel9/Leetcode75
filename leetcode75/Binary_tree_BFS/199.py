class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        from collections import deque
        queue = deque([root])
        rightSide = []
        
        while queue:
            levelLength = len(queue)  # Number of nodes at the current level
            for i in range(levelLength):
                node = queue.popleft()
                
                # If it's the last node of this level, add it to the rightSide list
                if i == levelLength - 1:
                    rightSide.append(node.val)
                
                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return rightSide
