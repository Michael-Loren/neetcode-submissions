class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cat = set()
        for num in nums:
            if num in cat:
                return True
            else:
                cat.add(num)

        return False
        