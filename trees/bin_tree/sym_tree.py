def sum_sym(root):
    if root is None:
        return 0
    right += sum_sym(root.right)
    left += sum_sym(root.left)
    if right == left:
        return True 


root = [1,2,2,3,4,4,3]
print(sum_sym(root))
