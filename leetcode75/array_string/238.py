class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_val = 1
        zero_cnt = 0
        zero_case = 0

        for i in range(len(nums)):
            if nums[i] ==0 and zero_cnt ==0:
                zero_cnt +=1
                # zero_case = total_val
                # total_val = total_val*nums[i]
            elif zero_cnt==1 and nums[i]==0:
                total_val = 0
            else:
                total_val = total_val*nums[i]


        new_list=[0]*len(nums)

        for i in range(len(nums)):
            if nums[i]==0 and zero_cnt==1:
                new_list[i] = total_val
            elif zero_cnt==1:
                new_list[i] = 0
            else: 
                new_list[i] = total_val/nums[i]
        
        return new_list