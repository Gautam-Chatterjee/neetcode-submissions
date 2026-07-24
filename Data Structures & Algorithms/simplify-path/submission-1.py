class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split("/")
        

        stack = []

        for curr in paths:
            if curr == "" or curr == ".":
                continue
            elif curr == "..":
               if stack: stack.pop()
            else:
                stack.append(curr)
        
        return "/"+ "/".join(stack)
               
    

        

            






        