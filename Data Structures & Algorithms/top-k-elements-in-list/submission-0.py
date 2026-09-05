class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = (counts.get(n, 0) + 1)
        
        buckets = [[] for _ in range(len(nums)+1)]

        for i in counts:
            buckets[counts[i]].append(i)
        

        results = []
        for i in range(len(buckets)-1, 0, -1):
            for n in buckets[i]:
                results.append(n)
            if len(results) == k:
                return results

        
