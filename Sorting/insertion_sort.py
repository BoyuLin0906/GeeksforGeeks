#Sort the array using insertion sort

class Solution:
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        for i in range(1, n):
            key_val = alist[i]
            
            j = i-1
            while j >= 0 and key_val < alist[j]:
                alist[j+1] = alist[j]
                j -= 1
                
            alist[j+1] = key_val

#Ref: https://www.geeksforgeeks.org/insertion-sort-algorithm/