#User function Template for python3

class Solution:
    def merge(self, arr, left, mid, right):
        left_arr_len = mid - left + 1
        right_arr_len = right - mid
        
        left_arr = [0] * left_arr_len
        right_arr = [0] * right_arr_len
        
        for i in range(left_arr_len):
            left_arr[i] = arr[left + i]
            
        for i in range(right_arr_len):
            right_arr[i] = arr[mid + 1 + i]
        
        left_idx = 0
        right_idx = 0
        arr_idx = left
        while left_idx < left_arr_len and right_idx < right_arr_len:
            if self.compare(left_arr[left_idx], right_arr[right_idx]):
                arr[arr_idx] = left_arr[left_idx]
                left_idx += 1
            else:
                arr[arr_idx] = right_arr[right_idx]
                right_idx += 1
            arr_idx += 1
            
        while left_idx < left_arr_len:
            arr[arr_idx] = left_arr[left_idx]
            left_idx += 1
            arr_idx += 1
        
        while right_idx < right_arr_len:
            arr[arr_idx] = right_arr[right_idx]
            right_idx += 1
            arr_idx += 1
        
        
    def mergeSort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2
            
            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid+1, right)
            self.merge(arr, left, mid, right)
    
    def compare(self, a, b):
        return a < b

#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends

# Ref: https://www.geeksforgeeks.org/merge-sort/