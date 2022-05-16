# Since a graph can have various components, we have to do
# the traversal on every component. Remember, even a single node
# which is not connected to any other nodes is also a component.

# suppose V here is no of nodes in the graph
# make a visited array 
visited = [0 for i in range(V)]
for i in range(V):
  if not visited[i]:
    dfsCall()
    # bfs()

# we will follow this structure every time
# assuming that the graph has multiple components.

# video: https://youtu.be/I6v0itcISSY
