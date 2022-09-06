class Solution:
    def rob(self, nums: List[int]) -> int:
        take, not_take = 0 , 0 
        for index in range(len(nums)):
            take, not_take = not_take + nums[index], max(take, not_take)
        return max(take, not_take)