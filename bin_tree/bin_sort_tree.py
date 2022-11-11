class BinarySortTree:
    def __init__(self,val):
        self.root = self.Node(val)
    class Node:
        def __init__(self,val,left=None,right=None):
            self.val = val
            self.left = left
            self.right = left
    def add_node(self,val):
        pass
        #Start from root which is initalized
    def contains(self,val,root=None):
        #dfs to look
        if not self.root:
            return False
        if self.root.val == val:
            return True
        return self.contains(self.root.left,val) or self.contains(self.root.right,val)

tree = BinarySortTree(13)
print(tree.contains(12))