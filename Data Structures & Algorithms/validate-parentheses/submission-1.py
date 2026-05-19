class Solution:
    def isValid(self, s: str) -> bool:
        strque = []

        for char in s:
            if char in ["[","{","("]:
                strque.append(char)

            else:
                if len(strque) > 0 and (char == "]" and strque[-1] == "[" or char == "}" and strque[-1] == "{" or char == ")" and strque[-1] == "("):
                    strque.pop(-1)

                else:
                    return False
        
        if len(strque) == 0:
            return True

        else:
            return False