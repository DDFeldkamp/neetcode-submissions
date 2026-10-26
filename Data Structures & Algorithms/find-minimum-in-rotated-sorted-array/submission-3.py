class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = 0
        max = len(nums) - 1
        mid = max//2
        prev = nums[mid]
        if mid == max:
            return nums[0]
        while min < max:
            if nums[min] > nums[mid]:
                max = mid
            elif nums[max] < nums[mid]:
                min = mid + 1
            else:
                return nums[min]
            mid = (max + min)//2
        return nums[min]



        

