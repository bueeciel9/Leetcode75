class Solution(object):
    def calcEquation(self, equations, values, queries):
        from collections import defaultdict

        # Step 1: Build the graph
        graph = defaultdict(dict)
        for (dividend, divisor), value in zip(equations, values):
            graph[dividend][divisor] = value
            graph[divisor][dividend] = 1 / value
        
        # Helper function for DFS
        def dfs(start, end, visited):
            if start not in graph or end not in graph:
                return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for neighbour, value in graph[start].items():
                if neighbour in visited:
                    continue
                visited.add(neighbour)
                d = dfs(neighbour, end, visited)
                if d != -1.0:
                    return d * value
            return -1.0
        
        # Step 2: Process queries
        results = []
        for query in queries:
            results.append(dfs(query[0], query[1], set()))
        
        return results
