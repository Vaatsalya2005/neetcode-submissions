class Solution:
    def isPalindrome(self, s: str) -> bool:
        t="".join(ch.lower() for ch in s if ch.isalnum())
        i=0
        j=len(t)-1
        while i<=j:
            if t[i] is t[j]:
                i+=1
                j-=1
            else:
                return False
        return True

        