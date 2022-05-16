# Adjaceny Matrix

n = int(input())
m = int(input())

# declare the adjacency matrix
adj = [[0 for j in range(n + 1)] for i in range(n + 1)]

# take edges as input
for i in range(m):
  u, v = map(int, input().split())
  # considering undirected graph
  adj[u][v] = 1
  adj[v][u] = 1
# Space Complexity: O(N^2)
# We can only use adjacency matrix for smaller values of n


# Adjacency List

n = int(input())
m = int(input())

# declaring the adjacency list
adjList = dict()

# take edges as input
for i in range(m):
  u, v = map(int, input().split())
  # considering undirected graph
  if u in adjList:
    adjList[u].append(v)
  else:
    adjList[u] = [v]
  
  if v in adjList:
    adjList[v].append(u)
  else:
    adjList[v] = [u]
    
# Space Complexity: O(N + 2*E)


# Video link: https://youtu.be/bTtm2ky7I3Y
