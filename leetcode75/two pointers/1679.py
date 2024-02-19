class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        from collections import Counter
        nums_count = Counter(nums)  # 각 숫자의 출현 횟수를 계산
        operations = 0
        
        for num in nums_count:
            complement = k - num  # 현재 숫자와 짝을 이루어 k를 만들 수 있는 수
            if complement in nums_count:  # 짝이 nums_count에 있는지 확인
                # 같은 숫자를 사용할 경우 또는 서로 다른 숫자를 사용할 경우 최소 횟수를 사용
                if complement == num:
                    operations += nums_count[num] // 2  # 같은 숫자를 사용하므로 절반만큼 연산 가능
                else:
                    operations += min(nums_count[num], nums_count[complement])  # 서로 다른 숫자를 사용할 경우 최소 출현 횟수만큼 연산 가능
                    # 한 쌍으로 사용된 숫자는 이후 계산에서 제외해야 하므로 출현 횟수를 0으로 설정
                    nums_count[complement] = 0
            nums_count[num] = 0  # 처리된 숫자는 0으로 설정하여 중복 계산 방지
        
        return operations