class Solution:
    def romanToInt(self, s: str) -> int:

        dic = {"I":1,"V":5, "X":10, "L": 50, "C":100, "D":500, "M":1000}

        val = 0
        for i,num in enumerate(s):
            if i< len(s)-1 and dic[num] < dic[s[i+1]]:
                val-=dic[num]
            else:
                val+=dic[num]
        return val
          

    



        