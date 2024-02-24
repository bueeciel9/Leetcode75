# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        def dfs(node):
            # If the node is None, return an empty list.
            if not node:
                return []
            # If the node is a leaf, return its value in a list.
            if not node.left and not node.right:
                return [node.val]
            # Otherwise, return the leaf values from the left and right subtrees.
            return dfs(node.left) + dfs(node.right)

        # Get the leaf value sequences of both trees.
        leaves1 = dfs(root1)
        leaves2 = dfs(root2)

        # Compare the two leaf value sequences.
        return leaves1 == leaves2
