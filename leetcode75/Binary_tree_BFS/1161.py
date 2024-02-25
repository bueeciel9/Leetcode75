from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        if not root:
            return 0
        
        queue = deque([root])  # Initialize the queue with the root
        max_sum = float('-inf')  # Initialize max_sum to the smallest number
        max_level = 1  # The level with the max sum
        current_level = 1  # Start from level 1
        
        while queue:
            level_sum = 0  # Sum of values for the current level
            level_length = len(queue)  # Number of nodes at the current level
            
            for _ in range(level_length):
                node = queue.popleft()  # Get the next node in the queue
                level_sum += node.val  # Add its value to the level sum
                
                # Add the node's children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # Check if the current level has the maximum sum so far
            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level
            
            current_level += 1  # Move to the next level
        
        return max_level
