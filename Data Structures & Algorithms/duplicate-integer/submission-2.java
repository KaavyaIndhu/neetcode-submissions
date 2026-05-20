class Solution {
    public boolean hasDuplicate(int[] nums) {
        //int[] nums = [1,2,3,4];
        HashSet<Integer> h=new HashSet<>();
        for (int i=0;i<nums.length;i++)
        {
            if(h.contains(nums[i]))
            {
                return true;
            }
            h.add(nums[i]);
        }
        return false;
    }
}