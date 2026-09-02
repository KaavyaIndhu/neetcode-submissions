class Solution:
    def rob(self, nums: List[int]) -> int:
        x=0
        y=0
        for n in nums:
            tmp=max(n+x,y)
            x=y
            y=tmp
        
        return y