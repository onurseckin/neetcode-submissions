from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sd = defaultdict(int)
        td = defaultdict(int)

        for c in s:
            sd[c] += 1

        for c in t:
            td[c] += 1 

        for c in t:
            if sd[c] != td[c]:
                return False

        return True

        