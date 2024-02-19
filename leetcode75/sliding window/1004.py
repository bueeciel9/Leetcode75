class Solution(object):
    def longestOnes(self, nums, k):
        left = 0  # 윈도우의 시작 포인터
        max_length = 0  # 최대 길이
        zeros = 0  # 윈도우 내 0의 개수

        for right in range(len(nums)):
            # 윈도우 오른쪽 끝의 요소가 0이면 0의 개수를 증가시킵니다.
            if nums[right] == 0:
                zeros += 1
            
            # 윈도우 내 0의 개수가 k를 초과하면, 왼쪽 끝을 오른쪽으로 이동시키면서 0의 개수를 조절합니다.
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            # 현재 윈도우의 길이를 계산하고 최대 길이를 업데이트합니다.
            max_length = max(max_length, right - left + 1)

        return max_length
