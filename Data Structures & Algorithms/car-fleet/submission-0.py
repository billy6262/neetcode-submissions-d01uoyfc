class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(speed)):
            cars.append((position[i],speed[i]))

        cars.sort(reverse = True)

        packs = 1
        leadTime = (target - cars[0][0]) / cars[0][1]
        for car in cars:
            time = (target - car[0]) / car[1]

            if time > leadTime:
                leadTime = time
                packs += 1

        return packs