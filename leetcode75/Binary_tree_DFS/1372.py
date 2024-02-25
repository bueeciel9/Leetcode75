class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def longestZigZag(self, root):
        self.max_length = 0

        def dfs(node, isLeft, length):
            if not node:
                return
            self.max_length = max(self.max_length, length)
            # If the last move was to the left, go right
            if isLeft:
                dfs(node.right, False, length + 1)
                dfs(node.left, True, 1)  # Reset length if direction changes
            else:
                dfs(node.left, True, length + 1)
                dfs(node.right, False, 1)  # Reset length if direction changes

        dfs(root.left, True, 1)  # Start by moving to the left
        dfs(root.right, False, 1)  # Start by moving to the right
        return self.max_length
