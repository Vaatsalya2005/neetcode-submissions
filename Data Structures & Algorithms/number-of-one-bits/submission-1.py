class Solution:
    def hammingWeight(self, n: int) -> int:
        # n & (n-1) 去掉最低位的1
        res = 0
        while n:
            n &= n - 1
            res += 1
        return res

'''
        x=bin(n)
        return x.count('1')

 '''       