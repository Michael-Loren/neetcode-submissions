class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cat = {}
        for num in nums:
            if num in cat:
                return True
            else:
                cat[num] = 0

        return False
        