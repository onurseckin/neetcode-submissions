class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        curr, subsets = [], []
        self.helper(0, nums, curr, subsets)
        return subsets

    def helper(self, i, nums, curr, subsets):
        if i >= len(nums):
            subsets.append(curr.copy())
            return

        curr.append(nums[i])
        self.helper(i+1, nums, curr, subsets)
        curr.pop()

        while i + 1 < len(nums) and nums[i] == nums[i+1]:
            i += 1

        self.helper(i+1, nums, curr, subsets)