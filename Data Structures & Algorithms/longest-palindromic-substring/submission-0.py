class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left:int,right:int)->str:
            while left>=0 and right< len(s) and s[left]==s[right]:
                left-=1
                right+=1
            return s[left+1:right]
        maxlen=0
        result=""
        for i in range (len(s)):
            odd=expand(i,i)
            even=expand(i,i+1)

            if len(odd)> maxlen:
                maxlen=len(odd)
                result=odd
            
            if len(even)>maxlen:
                maxlen=len(even)
                result=even
        return result