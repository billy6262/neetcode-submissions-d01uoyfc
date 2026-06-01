from sortedcontainers import SortedList
class MyCalendar:

    def __init__(self):
        self.cal = SortedList()

    def book(self, startTime: int, endTime: int) -> bool:
        i = self.cal.bisect_left((startTime,endTime))

        if i > 0 and self.cal[i - 1][1] > startTime:
            return False
        if i < len(self.cal) and self.cal[i][0] < endTime:
            return False
        self.cal.add((startTime,endTime))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)