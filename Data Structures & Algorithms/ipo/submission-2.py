class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = []

        for i in range(len(profits)):
            projects.append((profits[i],capital[i]))

        projects.sort(reverse = True)

        for i in range(k):
            for p in projects:
                if p[1] <= w:
                    w += p[0]
                    projects.remove(p)
                    break
        return w