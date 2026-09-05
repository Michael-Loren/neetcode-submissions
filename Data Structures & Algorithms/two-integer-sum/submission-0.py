class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = {}
        
        for i, num in enumerate(nums):
            needed = target - num
            if needed in first:
                return [first[needed], i]
            first[num] = i
        return []