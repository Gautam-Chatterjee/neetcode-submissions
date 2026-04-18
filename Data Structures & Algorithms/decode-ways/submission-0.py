class Solution:
    def numDecodings(self, s: str) -> int:
        self.num = 0

        def dfs(st):
            if st == "":
                self.num+=1
                return 
            else:
                if int(st[0]) in range(1,27):
                    dfs(st[1:])
                if st[0]!= "0" and len(st)>1 and int(st[0]+st[1]) in range(1,27):
                    dfs(st[2:])
        dfs(s)
        return self.num

