class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        cnt = 0
        flowerbed = [0] + flowerbed + [0]  # 경계 조건 처리를 위해 양쪽에 0 추가

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1]==0 and flowerbed[i] ==0 and flowerbed[i+1]==0:
                flowerbed[i]=1
                cnt +=1

        return cnt >= n

