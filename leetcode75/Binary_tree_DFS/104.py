# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Base case: If the root is None, then the depth is 0.
        if not root:
            return 0
        
        # Recursively find the depth of the left and right subtrees.
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        
        # The depth of the current tree is the max of left_depth and right_depth plus 1 (for the current node).
        return max(left_depth, right_depth) + 1
