class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        mapp = {"}":"{","]":"[",")":"("}
        stack = []
        for c in s:
            if c in ["[","{","("]:
                stack.append(c)
            elif stack and stack[-1]==mapp[c]:
                curr = stack.pop()
            else:
                return False
        if stack:
            return False
        return True 


            
        