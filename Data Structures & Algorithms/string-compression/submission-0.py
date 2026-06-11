class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []

        cur = chars[0]
        count = 0
        for char in chars + [None]:
            if char == cur:
                count += 1
            else:
                s.append(cur)
                if count > 1:
                    scount = str(count)
                    for n in scount:
                        s.append(n)
                cur = char
                count = 1
        chars[:] = s
        return len(s)