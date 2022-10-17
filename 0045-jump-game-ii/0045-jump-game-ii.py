class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        distance = 0
        curr_pos = 0
        n = len(nums)-1
        for i in range(n):
            distance = max(i+nums[i],distance)
            if curr_pos == i:
                curr_pos = distance
                count+=1
        return count