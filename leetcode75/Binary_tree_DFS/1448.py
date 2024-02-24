# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, max_val):
            if not node:
                return 0
            # Increment count if node.val >= max_val.
            count = 1 if node.val >= max_val else 0
            # Update max_val for the path to the current node.
            new_max = max(max_val, node.val)
            # Continue DFS traversal for left and right children.
            count += dfs(node.left, new_max)
            count += dfs(node.right, new_max)
            return count
        
        # Initialize the DFS with the root's value as the initial max_val.
        return dfs(root, root.val)
