class Solution:
    def checkValidString(self, s: str) -> bool:
        paran_stack = []
        star_stack = []

        for i in range(len(s)):
            if s[i] == "(":
                paran_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if paran_stack:
                    paran_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False
        

        while paran_stack and star_stack:
            paran_idx = paran_stack.pop()
            star_idx = star_stack.pop()
            if paran_idx > star_idx:
                return False
        
        return len(paran_stack) == 0