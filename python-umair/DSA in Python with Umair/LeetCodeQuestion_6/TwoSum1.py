# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

from typing import List


def twoSum( nums: List[int], target: int) -> List[int]:
        a = 0
        b = 1
        while a<b:
            if nums[a]+nums[b] == target:
                return [a,b]
            b = b + 1
            if b == len(nums):
                a = a + 1
                b = a + 1

nums = [20,7,11,15,2]
target = 9

print(twoSum(nums,target))