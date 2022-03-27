class Solution(object):
    def twoSum(self, arr, target):
        lis=[]
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[i]+arr[j]==target:
                    lis.append(i)
                    lis.append(j)
                    return lis