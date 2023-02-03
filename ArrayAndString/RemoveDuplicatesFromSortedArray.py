class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = len(nums)
        curIndex = 1
        for i in range(1, count):
            if nums[i - 1] != nums[i]:      
                nums[curIndex] = nums[i] 
                curIndex +=  1       
        return curIndex
