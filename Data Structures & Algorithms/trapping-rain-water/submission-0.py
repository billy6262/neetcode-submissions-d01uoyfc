class Solution:
    def trap(self, height: List[int]) -> int:
        H = height
        L = 0
        R = len(H) - 1
        MHL = H[L]
        MHR = H[R]
        watter = 0

        while L < R:
            if MHL > MHR:
                mwat = MHR - H[R]
                if mwat > 0:
                    watter += mwat
                R -= 1
                MHR = max(MHR,H[R])

            if MHL <= MHR:
                mwat = MHL - H[L]
                if mwat > 0:
                    watter += mwat
                L += 1
                MHL = max(MHL,H[L])

        
        return watter





        
