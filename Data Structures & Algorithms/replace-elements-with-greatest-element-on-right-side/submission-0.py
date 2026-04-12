class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        M = arr[-1]

        while i >= 0:
            if arr[i] < M:
                arr[i] = M

            if arr[i] > M:
                t = arr[i]
                arr[i] = M
                M = t
            i -= 1
        arr[-1] = -1
        return arr

