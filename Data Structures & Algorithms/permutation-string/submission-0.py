class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        counts = defaultdict(int)
        for i in s1:
            counts[i] = counts.get(i, 0) + 1
        

        counts2 = defaultdict(int)
        for r in range(len(s2)):

            if r - l + 1 > len(s1):
                l += 1
        
            if r - l + 1 == len(s1):
                for i in s2[l:r+1]:
                    counts2[i] = counts2.get(i, 0) + 1
                if counts2 == counts:
                    return True
                else:
                    counts2.clear()
        return False


