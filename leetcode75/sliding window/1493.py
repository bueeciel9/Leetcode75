class Solution(object):
    def longestSubarray(self, nums):
        left = 0  # 슬라이딩 윈도우의 시작점
        max_length = 0  # 최대 길이
        zero_count = 0  # 윈도우 내 0의 개수

        for right in range(len(nums)):
            # 현재 요소가 0이면, 0의 개수를 증가시킵니다.
            if nums[right] == 0:
                zero_count += 1
            
            # 윈도우 내 0의 개수가 2개가 되면, 윈도우의 시작점을 조정합니다.
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            
            # 최대 길이를 업데이트합니다. 여기서 right - left는 삭제된 요소를 고려하지 않은 길이이므로 +1을 하지 않습니다.
            max_length = max(max_length, right - left)

        return max_length
