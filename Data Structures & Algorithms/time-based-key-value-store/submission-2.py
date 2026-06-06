class TimeMap:

    def __init__(self):
        self.keymap = dict([])

    def set(self, key: str, value: str, timest: int) -> None:
        keys = self.keymap.get(key,[]).copy()
        keys.append((timest,value))
        self.keymap[key] = keys

    def get(self, key: str, timest: int) -> str:
        if key not in self.keymap:
            return ""
        keys = self.keymap[key]
        L = 0
        R = len(keys) - 1

        curr = None
        while L <= R:
            mid = (R + L) // 2
            if keys[mid][0] == timest:
                return keys[mid][1] 
            if keys[mid][0] < timest:
                curr = keys[mid][1]
                L = mid + 1
            else:
                R = mid - 1
        if not curr:
            return ""
        return curr