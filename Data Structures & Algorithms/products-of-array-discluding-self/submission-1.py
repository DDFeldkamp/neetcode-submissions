class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prod = 1
        prod_zero_i = -1
        for i in range(n):
            if nums[i] == 0:
                if prod_zero_i != -1:
                    return [0] * n
                else:
                    prod_zero_i = i
            else:
                prod *= nums[i]
       
        if prod_zero_i != -1:
            prods = [0] * n
            prods[prod_zero_i] = prod
        else:
            prods = [prod] * n
            for i in range(n):
                prods[i] //= nums[i]
        return prods