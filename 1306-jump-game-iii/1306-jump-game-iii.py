class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        queue = deque()
        queue.append(start)
        visited = set()
        n = len(arr)
        
        while queue:
            idx = queue.popleft()
            
            if idx in visited:
                continue
            visited.add(idx)
            
            if arr[idx] == 0:
                return True
            else:
                if idx - arr[idx] >= 0:
                    queue.append(idx - arr[idx])
                if idx + arr[idx] < n:
                    queue.append(idx + arr[idx])
        return False