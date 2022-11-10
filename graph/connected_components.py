def connected_components_count(graph):
  visited = set()
  count = 0
  for node in graph:
    returned = traverse(node,graph,visited)
    if returned:
      count+= 1
  return count

def traverse(current,graph,visited):
    if current in visited:
        return False
    visited.add(current)
    for node in graph:
        traverse(node,graph,visited)
    return True


print(connected_components_count({
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}) # -> 2
)

