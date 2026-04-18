class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        for st in strs:
            count = [0] * 26
            for c in st:
                count[ord(c)-ord('a')]+=1
            if tuple(count) in mp:
                mp[tuple(count)].append(st)
            else:
                mp[tuple(count)] = []
                mp[tuple(count)].append(st)
        ans = []
        for val in mp.values():
            ans.append(val)

        return ans





        