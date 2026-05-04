class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dc = {}

        for n in nums:
            if n in dc:
                return True
            else:
                dc[n] = 'x'

        return False
        