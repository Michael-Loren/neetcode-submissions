class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)

        longest = 0
        for i in nums:
            if i - 1 not in nums:
                count = 0
                while i in nums:
                    count += 1
                    i += 1
                longest = max(longest, count)
        
        return longest
            


        
        