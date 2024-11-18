class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        leftPointer=0
        for rightPointer in range(len(nums)):
            if nums[rightPointer] != val:
                nums[leftPointer]=nums[rightPointer]
                leftPointer+=1
        return leftPointer
            



