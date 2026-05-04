class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dc = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in dc:
                return [dc[diff], i]
            dc[n] = i