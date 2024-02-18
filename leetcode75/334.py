class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')  # 무한대로 초기화하여 어떤 수보다도 크게 설정
        for n in nums:
            if n <= first:  # 현재 값이 'first'보다 작거나 같으면 'first'를 업데이트
                first = n
            elif n <= second:  # 현재 값이 'second'보다 작거나 같으면 'second'를 업데이트
                second = n
            else:  # 'first'와 'second'보다 큰 값이 나타나면 True 반환
                return True
                
        return False