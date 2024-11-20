def is_empty_tree(tree):
    return isinstance(tree, list) and not tree

def is_leaf(tree):
    return isinstance(tree, int)

def create_tree(left_subtree, key, right_subtree):
    return [left_subtree, key, right_subtree]

def left_subtree(tree):
    return tree[0]

def key(tree):
    if is_leaf(tree):
        return tree
    else:
        return tree[1]

def right_subtree(tree):
    return tree[2]