class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars=[]
        for ch in s:
            if ch.isalnum():
                chars.append(ch.lower())

        cleaned = "".join(chars)        

        return cleaned == cleaned[::-1]               
        