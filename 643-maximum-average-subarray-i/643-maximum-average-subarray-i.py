class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxs = ans = sum(nums[:k])
        for i, n in enumerate(nums[k:]):
            ans+= n - nums[i]
            maxs = max(maxs,ans)
        return maxs*1.0/k