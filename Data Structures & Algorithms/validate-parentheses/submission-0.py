class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hashSet= { ")":"(", "}":"{", "]": "["}
        for c in s:
            if c in hashSet:
                if stack and stack[-1]== hashSet[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

