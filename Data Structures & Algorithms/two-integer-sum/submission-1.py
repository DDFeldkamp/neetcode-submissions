class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ints = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in ints:
                return [ints[num], i]
            else:
                ints[target - num] = i
        