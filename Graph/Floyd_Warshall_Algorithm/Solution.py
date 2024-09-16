#User function template for Python
import math

class Solution:
	def shortest_distance(self, matrix):
		number_of_nodes = len(matrix)
		
		for i in range(number_of_nodes):
            for j in range(number_of_nodes):
                if matrix[i][j] == -1:
                    matrix[i][j] = math.inf
		
		for k in range(number_of_nodes):
		    for i in range(number_of_nodes):
                for j in range(number_of_nodes):
                    matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
        
        for i in range(number_of_nodes):
            for j in range(number_of_nodes):
                if matrix[i][j] == math.inf:
                    matrix[i][j] = -1
        
#{ 
 # Driver Code Starts
#Initial template for Python 

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		matrix = []
		for _ in range(n):
			matrix.append(list(map(int, input().split())))
		obj = Solution()
		obj.shortest_distance(matrix)
		for _ in range(n):
			for __ in range(n):
				print(matrix[_][__], end = " ")
			print()
# } Driver Code Ends

# Ref: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/