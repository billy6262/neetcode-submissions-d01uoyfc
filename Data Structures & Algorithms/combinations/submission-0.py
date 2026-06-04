class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        arr = []


        def helper(i: int, cur: List[int]):
            if i > n + 1:
                return
            if len(cur) == k:
                arr.append(cur.copy())
                return
            cur.append(i)
            helper(i + 1, cur)
            cur.pop()

            helper(i + 1, cur)

        helper(1, [])

        return arr