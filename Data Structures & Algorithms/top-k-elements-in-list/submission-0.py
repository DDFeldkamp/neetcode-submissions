import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lst = {}
        for i in nums:
            if i not in lst:
                lst[i] = 1
            else:
                lst[i] += 1
        to_Ret = []
        for i, _ in heapq.nlargest(k, lst.items(), key = lambda x: x[1]):
            to_Ret += [i]
        return to_Ret