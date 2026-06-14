class Solution:
    def countBits(self, n: int) -> List[int]:
        arr=[]
        for i in range(n+1):
            x=bin(i)
            s=x.count('1')
            arr.append(s)
        return arr

        