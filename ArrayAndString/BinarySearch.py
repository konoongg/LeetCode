class Solution:
    def search(self, nums, target):
        if target not in nums:
            return -1
        left = 0
        right = len(nums) - 1
        pvot = (left + right) // 2
        print(pvot)
        while nums[pvot] != target:
            if nums[pvot] < target:
                left = pvot + 1
                pvot = (left + right) // 2
            elif nums[pvot] > target:
                right = pvot 
                pvot = (left + right) // 2
        return pvot
