class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        arr = [0] * len(temps)

        for i,day in enumerate(temps):
            while stack and day > stack[-1][1]:
                ntemp = stack.pop()
                arr[ntemp[0]] = i - ntemp[0]
            stack.append((i,day))

        return arr

