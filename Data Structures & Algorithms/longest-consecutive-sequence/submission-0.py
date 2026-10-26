class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        set_nums = set()
        for val in nums:
            set_nums.add(val)
        curr_run = 1
        best_run = 1
        for i in set_nums:
            if i-1 not in set_nums:
                k = i + 1
                while k in set_nums:
                    curr_run += 1
                    k += 1
                best_run = max(curr_run, best_run)
                curr_run = 1
        return best_run

