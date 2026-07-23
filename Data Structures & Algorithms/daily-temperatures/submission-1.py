class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(0,temperatures[0])]
        result = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if stack:
                if stack[-1][1] >= temperatures[i]:
                    stack.append((i,temperatures[i]))

                else:
                    while stack and stack[-1][1] < temperatures[i]:
                        ntemp = stack[-1]
                        stack.pop()
                        result[ntemp[0]] = i-ntemp[0]
                    stack.append((i, temperatures[i]))
        return result
        


                  




        