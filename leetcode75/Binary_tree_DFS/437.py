# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        self.count = 0
        cache = {0: 1}  # Initialize cache with 0 sum having 1 occurrence.

        def dfs(node, currentSum):
            if not node:
                return
            
            # Update the current path sum.
            currentSum += node.val
            
            # Check if there's a prefix sum that equals currentSum - targetSum.
            self.count += cache.get(currentSum - targetSum, 0)
            # 예를 들어, cache.get(currentSum - targetSum, 0)는 currentSum - targetSum이라는 키로 cache에서 값을 조회합니다. 만약 이 키에 해당하는  값이 없다면, 0을 반환합니다. 이는 현재까지의 경로 합에서 targetSum을 뺀 값이 이전에 나타난 적이 없다는 것을 의미하므로, 이 경로를 타겟 합을 만족하는 경로로 계산할 수 없음을 의미합니다.
            # Update cache with the current path sum.
#             cache[currentSum] 업데이트
# cache[currentSum] = cache.get(currentSum, 0) + 1은 현재 경로의 합인 currentSum을 키로 가지는 항목의 값을 업데이트합니다. 만약 currentSum이 이미 cache에 있다면, 그 값에 1을 더합니다. 만약 없다면, currentSum을 새 키로 추가하고 값을 1로 설정합니다. 이는 현재 경로의 합이 새로운 경로의 합으로 등장했음을 의미하며, 나중에 같은 합을 가진 다른 경로를 찾을 때 이를 사용할 수 있습니다.
            cache[currentSum] = cache.get(currentSum, 0) + 1
            
            # Recurse down to children.
            dfs(node.left, currentSum)
            dfs(node.right, currentSum)
            
            # Remove the current path sum from the cache when going back up the recursive call stack.
#             cache[currentSum] -= 1
# 재귀 호출에서 돌아올 때 cache[currentSum] -= 1을 실행하는 이유는 현재 경로를 더 이상 고려하지 않기 위함입니다. 즉, 현재 경로의 합을 가진 경로의 개수를 하나 감소시킵니다. 이는 다른 경로를 탐색할 때, 현재 경로의 합이 영향을 미치지 않도록 하기 위한 것입니다. 만약 현재 경로가 다른 경로의 계산에 영향을 미친다면, 잘못된 결과를 얻을 수 있기 때문입니다.
            cache[currentSum] -= 1

        dfs(root, 0)
        return self.count
