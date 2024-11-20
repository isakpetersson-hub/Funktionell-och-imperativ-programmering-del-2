from tree_algoritms import *

def traverse(tree,inner_node_fn,leaf_fn,empty_tree_fn):
    if is_empty_tree(tree):
        return empty_tree_fn()
    elif isinstance(tree,list) and len(tree)==3:
        left_tree = left_subtree(tree)
        right_tree = right_subtree(tree)
        key_value = key(tree)
        left = traverse(left_tree,inner_node_fn,leaf_fn,empty_tree_fn)
        right = traverse(right_tree,inner_node_fn,leaf_fn,empty_tree_fn)
        return inner_node_fn(key_value,left,right)
    elif isinstance(tree,list):
        raise ValueError("felaktig format på listan")
    else:
        return leaf_fn(tree)

def empty_tree_fn():
    return 0

def leaf_fn(key):
    return key**2

def inner_node_fn(key,left_val,right_val):
    return key+left_val