def largest_component(graph):
  visited = set()
  largest = 0
  for node in graph:
    count_traversal = depth_search(node,graph,visited)
    print(count_traversal)
    if count_traversal > largest:
      largest = count_traversal
  return largest

#May need additional info in 
def depth_search(current,graph,visited):
    if current in visited:
        return 0
    visited.add(current)
    size = 1
    for node in graph[current]:
        size += depth_search(node,graph,visited=)
    return size

print(largest_component({
0: [8, 1, 5],
1: [0],
5: [0, 8],
8: [0, 5],
2: [3, 4],
3: [2, 4],
4: [3, 2]
})) # -> 4