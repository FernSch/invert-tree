
#invert a binary tree
def invert_tree(tree):
    if tree is None:
        return None
    else:
        tree.left, tree.right = tree.right, tree.left
        invert_tree(tree.left)
        invert_tree(tree.right)
        return tree
