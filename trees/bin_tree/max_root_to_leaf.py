#dfs
def max_path_sum(root):
  return _max_path_sum(root)

def _max_path_sum(root):
  if not root:
    return float("-inf")

  if root.left is None and root.right is None:
    return root.val
  
  left = _max_path_sum(root.left)
  right = _max_path_sum(root.right)
  return max(left,right)


class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

a = Node(5)
b = Node(11)
c = Node(54)
d = Node(20)
e = Node(15)
f = Node(1)
g = Node(3)

a.left = b
a.right = c
b.left = d
b.right = e
e.left = f
e.right = g

print(max_path_sum(a)) #59