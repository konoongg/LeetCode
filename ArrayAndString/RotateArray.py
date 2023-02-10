class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        size = len(nums)
        k = k % size 
        rotateNums = []
        for i in range(size  - k, size  ):
            rotateNums.append(nums[i])
        for i in range(0, size  - k):
            rotateNums.append(nums[i])
        for i in range(size):
            nums[i] = rotateNums[i]
        print(rotateNums)
