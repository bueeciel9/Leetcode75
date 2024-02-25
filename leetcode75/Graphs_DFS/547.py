class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)  # Number of cities
        visited = [False] * n  # Track visited cities
        provinces = 0  # Count of provinces

        def dfs(city):
            """Perform DFS to mark all cities connected to the current city."""
            for j in range(n):
                # If the city is connected and not visited
                if isConnected[city][j] == 1 and not visited[j]:
                    visited[j] = True  # Mark as visited
                    dfs(j)  # Visit all cities connected to city j

        for i in range(n):
            # If the city i has not been visited, it's a new province
            if not visited[i]:
                dfs(i)  # Perform DFS starting from city i
                provinces += 1  # Increase the province count

        return provinces
