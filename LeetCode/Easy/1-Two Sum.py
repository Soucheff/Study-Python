#https://leetcode.com/problems/two-sum/

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    index=0
    i=nums.pop(0)
    for j in range(i+1,total):
        if nums[i]+nums[j] == target:
            return [i,j]
            
nums = [3,2,3]
print(twoSum(nums,6))