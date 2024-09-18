#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self, arr, n):
        
        for i in range(n-1):
            
            is_update = False
            
            for j in range(n-1-i):
                if self.compare(arr[j], arr[j+1]):
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    is_update = True
                    
            if not is_update:
                break
                
    def compare(self, a, b):
        return a > b


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends


# Ref: https://www.geeksforgeeks.org/bubble-sort-algorithm/