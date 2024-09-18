#User function Template for python3

class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self, arr, low, high):
        if low < high:
            pivot_idx = self.partition(arr, low, high)
            
            self.quickSort(arr, low, pivot_idx-1)
            self.quickSort(arr, pivot_idx+1, high)
        
    
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if self.compare(arr[j], pivot):
                i += 1
                self.swap(arr, i, j)
        
        # povit swap
        i += 1
        self.swap(arr, i, high)
        return i
    
    def compare(self, a, b):
        return a < b
    
    def swap(self, arr, a, b):
        arr[a], arr[b] = arr[b], arr[a]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends

# Ref: https://www.geeksforgeeks.org/quick-sort-algorithm/