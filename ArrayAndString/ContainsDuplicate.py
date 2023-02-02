class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        collection = set()
        for i in nums:
            if i in collection:
                return True
            else:
                collection.add(i)
        return False
      
     """
     SECOND VERSION, slower but requires less memory
     class Solution:
      def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
     """
"""
https://leetcode.com/problems/contains-duplicate/description/
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""
