class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = {}
        for s in strs:
            curr_lets = [0] * 26
            for l in s:
                curr_lets[ord(l) - ord('a')]+=1
            curr_lets = tuple(curr_lets)
            if curr_lets in ans:
                ans[curr_lets] += [s]
            else:
                ans[curr_lets] = [s]
        return list(ans.values())
