class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        for i in range(len(filtered) // 2):
            j = (len(filtered)-1) - i
            
            if filtered[i] != filtered[j]:
                return False
        
        return True