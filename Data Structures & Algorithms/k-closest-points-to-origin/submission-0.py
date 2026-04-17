import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        arr = []

        for i in range(len(points)):
            arr.append([i,math.sqrt(pow(points[i][0],2) + pow(points[i][1],2))])

        arr.sort(key = lambda x : x[1])

        i = 0
        ret = []
        while i < k:
            ret.append(points[arr[i][0]])
            i += 1

        return ret