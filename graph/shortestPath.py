def shortest_path(edges, node_A, node_B):
  graph = {}
  for pairs in edges:
    a,b = pairs
    if a not in graph:
      graph[a] = []
    if b not in graph:
      graph[b] = []
    graph[a].append(b)
    graph[b].append(a)
  return path_nodes(graph, node_A, node_B,set([node_A, 0]))
  
def path_nodes(graph,start,end,visited):
  from collections import deque
  queue = deque([(start, 0)])
  while queue:   
    current, dist = queue.popleft()
    if current == end:
      return dist
    for node in graph[current]:
      if node not in visited:
        visited.add(current)
        queue.append((node,dist+1))
  return -1
      
#Shortest path should use breadth first
edges = [
  ['w', 'x'],
  ['x', 'y'],
  ['z', 'y'],
  ['z', 'v'],
  ['w', 'v']
]

print(shortest_path(edges, 'w', 'z')) # -> 2