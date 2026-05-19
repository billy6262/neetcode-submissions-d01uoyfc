class Solution:
    def climbStairs(self, n: int) -> int:
        mem = {}
        def recu(n):
            if n in mem:
                return mem[n]
            if  n <= 2:
                return n # final call in 1 or less steps remain

            mem[n] = recu(n - 1) + recu(n - 2)

            return mem[n]
        
        return recu(n)