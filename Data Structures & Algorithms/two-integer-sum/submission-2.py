class Solution :
    def twoSum(self, nums, target):
        prevMap = dict()
        for i, n in enumerate(nums):
            diff= target- nums[i]
            if diff in prevMap:
                return list((prevMap[diff], i))
            prevMap[n] = i      
               
