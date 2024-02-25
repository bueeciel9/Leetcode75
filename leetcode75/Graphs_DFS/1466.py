class Solution(object):
    def minReorder(self, n, connections):
        # Create a graph where each node keeps track of which connections need reversing
        graph = {i: [] for i in range(n)}
        for a, b in connections:
            graph[a].append((b, 1))  # 1 indicates the edge needs reversal
            graph[b].append((a, 0))  # 0 indicates no reversal needed

        def dfs(city, parent):
            reversals = 0
            for neighbor, needs_reversal in graph[city]:
                if neighbor == parent:
                    continue
                reversals += needs_reversal
                reversals += dfs(neighbor, city)
            return reversals
        
        return dfs(0, -1)
