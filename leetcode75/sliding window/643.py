class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        value =0 

        for i in range(k):
            value = value + nums[i]
        max_value =value

        for i in range(k, len(nums)):
            value = value-nums[i-(k)]+nums[i]
            max_value = max(value, max_value)

        result = float(max_value)/k
        return result