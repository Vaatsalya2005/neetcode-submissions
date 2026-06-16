class Solution:
    def isHappy(self, n: int) -> bool:
        s=[int(d) for d in str(n)]
        seen=[]
        add=0
        while s:
            for x in s:
                add+=x*x
            if add in seen:
                return False
            elif add==1:
                return True
            seen.append(add)
            s=[int(d) for d in str(add)]
            add=0



        