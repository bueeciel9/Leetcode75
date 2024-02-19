class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        lastNonZeroFoundAt = 0
        # 모든 0이 아닌 요소를 앞으로 이동
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZeroFoundAt] = nums[i]
                lastNonZeroFoundAt += 1
        
        # 나머지 요소를 0으로 설정
        for i in range(lastNonZeroFoundAt, len(nums)):
            nums[i] = 0

        return nums