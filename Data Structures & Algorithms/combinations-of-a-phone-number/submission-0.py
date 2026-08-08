class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl","6":"mno","7":"pqrs", "8":"tuv", "9": "wxyz"}
        
        if digits == "": return []
        res = []
        def backtrack(i, arr):
            if len(arr) == len(digits):
                res.append("".join(arr))
                return
            
            for c in mp[digits[i]]:
                arr.append(c)
                backtrack(i+1, arr)
                arr.pop()
        

        backtrack(0, [])
        return res

           


            


