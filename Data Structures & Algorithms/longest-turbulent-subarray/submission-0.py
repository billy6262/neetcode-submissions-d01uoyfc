class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:

        if len(arr) < 2:
            return len(arr)
        mlen = 1
        currlen = 1

        greaterRight = None

        for R in range(len(arr) - 1):
            if arr[R] == arr[R + 1]:
                currlen = 1
                greaterRight = None

            elif greaterRight is True:
                if arr[R] < arr[R + 1]:
                    currlen += 1
                    greaterRight = False

                else:
                    greaterRight = True
                    currlen = 2

            elif greaterRight is False:
                if arr[R] > arr[R + 1]:
                    currlen += 1
                    greaterRight = True

                else:
                    greaterRight = False
                    currlen = 2
            elif greaterRight == None:
                currlen = 2
                greaterRight = arr[R] > arr[R + 1]
            mlen = max(mlen, currlen)

        return mlen

                

