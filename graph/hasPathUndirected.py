#Will be in infinite loop back and forth
#Need to save traversed path
def undirected_path(edges,start,end):
  graph = {}
  for pair in edges:
      first,second = pair
      if first not in graph:
          graph[first] = []
      if second not in graph:
          graph[second] = [] 
      graph[first].append(second)
      graph[second].append(first)
  return graph
      
def find_path_depth(graph,current,end,a=[]):
    if current == end:
        return True
    if current in a:
        return True 
    a.append(current)
    for node in graph[current]:
        if find_path(graph,node,end) == True:
            return True
    return False

def find_path_breadth(graph,start,end,a=[]):
    from collections import deque
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == end:
            return True
        if current in a:
            current = queue.popleft()
        a.append(current)
        for node in graph[current]:
            queue.append(node)
    return False
      
def undirected_depth(edges,start,end):
    directed = undirected_path_depth(edges,start,end)
    return find_path_depth(directed,start,end)


def undirected_breadth(edges,start,end):
    directed = undirected_path(edges,start,end)
    return find_path_breadth(directed,start,end)


edges = [
  ('b', 'a'),
  ('c', 'a'),
  ('b', 'c'),
  ('q', 'r'),
  ('q', 's'),
  ('q', 'u'),
  ('q', 't'),
]


print(undirected_breadth(edges, 'j', 'm')) # -> True
# print(undirected_depth(edges, 'j', 'm')) # -> True