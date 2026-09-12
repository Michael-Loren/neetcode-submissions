class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0

        base = defaultdict(int)
        counts = defaultdict(int)
        
        for i in s1:
            base[i] += 1
        


        for r in range(len(s2)):
            
            counts[s2[r]] += 1

            if r - l + 1 > len(s1):
                counts[s2[l]] -= 1
                if counts[s2[l]] == 0:
                    del counts[s2[l]]
                l += 1
            if counts == base:
                return True
        
        return False
                




