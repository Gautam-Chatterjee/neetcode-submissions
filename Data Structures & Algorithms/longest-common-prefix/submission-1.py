class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common  = ""
        i = 0
        while True:
            if i < len(strs[0]):
                curr = strs[0][i]
            for string in strs:
                if i < len(string) and string[i] == curr:
                    continue
                else:
                    return common
            common += curr
           
            i+=1
            print(i)

        return common 
