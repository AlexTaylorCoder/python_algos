def has_path_depth(graph, src, dst):
    if src == dst:
        return True
    for i in graph[src]:
        if has_path(graph, i,dst):
            return True
    return False


def has_path_breadth(graph, src, dst):
    from collections import deque
    queue = deque([src])
    while queue:
        current = queue.popleft()
        if current == dst:
            return True 
        for i in graph[current]:
            queue.append(i)
            




graph = {
  'v': ['x', 'w'],
  'w': [],
  'x': [],
  'y': ['z'],
  'z': [],  
}

print(has_path_breadth(graph, 'v', 'w'))
# print(has_path_depth(graph, 'v', 'w')) # True