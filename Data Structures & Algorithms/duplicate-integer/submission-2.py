from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dc = defaultdict(int)

        for n in nums:
            if n in dc:
                return True
            dc[n] += 1
        
        return False
        