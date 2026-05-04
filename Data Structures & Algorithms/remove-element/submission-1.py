class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = len(nums)
        count = 0
        for i in range(length):
            if nums[i] == val:
                count += 1
            elif count > 0:
                nums[i-count] = nums[i]
        
        if count > 0:
            del nums[-count:]

        return length - count

        