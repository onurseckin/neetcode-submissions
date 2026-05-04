class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        highest = 0

        for i in nums:
            if i == 1:
                current += 1
            else:
                highest = max(current, highest)
                current = 0

        return max(highest, current)
        