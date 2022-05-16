class Solution:
    def recursion(self,idx,arr,n,maxx,size,k):
        if idx == n:
            return maxx * size  
        if (idx,size,maxx) in self.dp: return self.dp[(idx,size,maxx)]
        ch1 = self.recursion(idx+1,arr,n,max(maxx,arr[idx]),size+1,k) if size < k else 0
        ch2 = self.recursion(idx+1,arr,n,arr[idx],1,k) + maxx*size
        best = ch1 if ch1 > ch2 else ch2
        self.dp[(idx,size,maxx)] = best
        return best
        
        
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        self.dp = {}
        return self.recursion(1,arr,len(arr),arr[0],1,k)