from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc = {}
        for idx, n in enumerate(nums):
            diff = target - n
            if diff in dc:
                return [dc[diff], idx]
            dc[n] = idx
