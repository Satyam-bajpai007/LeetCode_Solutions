class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n=len(arr)
        visited=set()
        
        def helper(start,visited):
            
            if start<0 or start>n-1:
                return False
            
            if start in visited:
                return False  
            
            if arr[start] == 0:
                return True
            
            visited.add(start)
            
            high = helper(start + arr[start],visited)
            low = helper(start - arr[start],visited)
            
            return high or low
        
        return helper(start,visited)