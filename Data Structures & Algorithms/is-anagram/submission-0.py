class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num = {}
        for i in s:
            if i not in num:
                num[i] = 1
            else:
                num[i] += 1
        for i in t:
            if i not in num:
                return False
            else:
                num[i] -= 1
        for i in num.values():
            if i != 0:
                return False
        return True
        