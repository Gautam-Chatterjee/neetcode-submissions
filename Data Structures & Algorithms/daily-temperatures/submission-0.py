class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []

        for idx, t in enumerate (temperatures):
            while stack and t>stack[-1][0]:
                curr = stack.pop()
                res[curr[1]] = idx - curr[1]
            stack.append([t,idx]) 
        return res
        