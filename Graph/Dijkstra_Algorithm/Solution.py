from typing import List
import math
class Solution:
    
    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, V: int, adj: List[List[int]], S: int) -> List[int]:
    # Code here
        dist = [math.inf] * V
        dist[S] = 0
        visited = [False] * V
        for _ in range(V):
            curr_idx = self.get_min_distance_node(dist, visited, V)
            visited[curr_idx] = True
            
            for next_node in adj[curr_idx]:
                next_node_idx = next_node[0]
                next_node_dist = next_node[1]
                if dist[next_node_idx] > dist[curr_idx] + next_node_dist and not visited[next_node_idx]:
                    dist[next_node_idx] = dist[curr_idx] + next_node_dist
        
        return dist
                
        
        
    def get_min_distance_node(self, dist: List[int], visited: List[bool], V: int) -> int:
        
        min_val = math.inf
        min_index = -1
        
        for node_idx in range(V):
            if dist[node_idx] < min_val and not visited[node_idx]:
                min_val = dist[node_idx]
                min_index = node_idx
        
        return min_index
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V, E = map(int, input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        S = int(input())
        ob = Solution()

        res = ob.dijkstra(V, adj, S)
        for i in res:
            print(i, end=" ")
        print()

# } Driver Code Ends

# Ref: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/