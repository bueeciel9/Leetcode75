class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        n = len(grid)  # 행렬의 크기
        count = 0  # 동일한 행과 열의 쌍의 수
        
        # 열을 리스트로 변환
        columns = [[grid[i][j] for i in range(n)] for j in range(n)]
        
        # 각 행에 대해 모든 열과 비교
        for i in range(n):
            for j in range(n):
                if grid[i] == columns[j]:  # 행과 열이 동일한지 직접 비교
                    count += 1
                    
        return count
