class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob1(arr:List[int])->int:
            x=0
            y=0
            for n in arr:
                temp=max(n+x,y)
                x=y
                y=temp
            return y
        length=len(nums)
        if length==1:
            return nums[0]
        val1= rob1(nums[0:length-1])
        val2= rob1(nums[1:])
        return max(val1,val2)

        