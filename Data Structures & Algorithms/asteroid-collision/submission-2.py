class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        carr = []
        rarr = []

        nums = asteroids

        for num in nums:
            if num > 0:
                carr.append(num)

            elif num < 0:
                if len(carr) > 0:
                    while len(carr) > 0:

                        if abs(num) > carr[-1]:
                            carr.pop(-1)

                            if len(carr) == 0:
                                rarr.append(num)

                        elif carr[-1] == abs(num):
                            carr.pop(-1)
                            break
                    
                        elif abs(num) < carr[-1]:
                            break
                else:
                    rarr.append(num)

        return rarr + carr