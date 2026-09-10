class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMin=curMax=1
        for n in nums:
            if n==0:
                curMin=curMax=1
                continue
            tmp=curMax
            curMax=max(n,n*curMax,n*curMin)
            curMin=min(n,n*tmp,n*curMin)
            res=max(curMax,res)
        return res