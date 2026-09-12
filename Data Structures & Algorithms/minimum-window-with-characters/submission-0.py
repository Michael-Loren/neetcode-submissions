class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        window = defaultdict(int)
        need = defaultdict(int)
        
        for c in t:
            need[c] += 1

        required = len(need)
        have = 0
        l = 0
        best_len = float("inf")
        best_l = 0

        for r, c in enumerate(s):
            window[c] += 1


            if c in need and window[c] == need[c]:
                have += 1
            
            while have == required:
                window_len = r - l + 1
                
                if window_len < best_len:
                    best_len = window_len
                    best_l = l
                
                left = s[l]
                window[left] -= 1
                
                if left in need and window[left] < need[left]:
                    have -= 1
            
                l += 1
        if best_len == float("inf"):
            return ""
        
        return s[best_l:best_l + best_len]


