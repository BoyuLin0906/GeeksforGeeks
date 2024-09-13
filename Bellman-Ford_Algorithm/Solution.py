#User function Template for python3

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''
    def bellman_ford(self, V, edges, S):
        #code here
        dist = [100000000] * V
        dist[S] = 0
        
        for node in range(V - 1):
            # relaxing
            for n_from, n_to, weight in edges:
                if dist[n_from] != 100000000 and dist[n_from] + weight < dist[n_to]:
                     dist[n_to] = dist[n_from] + weight
        
        # find negative cycle
        for n_from, n_to, weight in edges:
            if dist[n_from] != 100000000 and dist[n_from] + weight < dist[n_to]:
                return [-1]
                
        return dist
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        edges = []
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            edges.append([u,v,w])
        S=int(input())
        ob = Solution()
        
        res = ob.bellman_ford(V,edges,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends

# Ref: https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/