class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        for i in nums:
            total *= i
        
        res = []
        for i in range(len(nums)):
            if nums[i] == 0:
                temp = 1
                for j in range(len(nums)):
                    if j != i:
                        temp *= nums[j]
                res.append(temp)
            else:
                res.append(total // nums[i])
        
        return res

        