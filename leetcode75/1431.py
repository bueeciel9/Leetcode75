class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        maxCandies = max(candies)  # 모든 아이들 중 가장 많은 사탕의 수를 찾습니다.
        result = [candy + extraCandies >= maxCandies for candy in candies]  # 각 아이에 대한 결과를 계산합니다.
    
        return result

