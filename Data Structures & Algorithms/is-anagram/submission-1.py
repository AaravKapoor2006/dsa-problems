class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        elements=list(s)
        
        for char in t:
            if char not in elements:
                return False
            elements.remove(char)
        
        return True