class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        greatest = arr[n-1]
        arr[n-1] = -1

        for i in range(n-2, -1, -1):
            current = arr[i]
            arr[i] = greatest
            if current > greatest:
                greatest = current

        return arr
