class Solution(object):
    def applyOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range (len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
       
        non_zero_index = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1

        while non_zero_index < len(nums):
            nums[non_zero_index] = 0
            non_zero_index += 1
        return nums

            

        