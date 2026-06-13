class Solution:
    def isValid(self, s: str) -> bool:
        d={
            ']':'[',
            '}':'{',
            ')':'('
        }
        stack=[]
        for c in s:
            if stack and d.get(c,0)==stack[-1]:
                stack.pop()
            else:
                stack.append(c) 
        return not stack
        