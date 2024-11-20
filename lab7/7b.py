from tree_algoritms import *

def traverse(tree,inner_node_fn,leaf_fn,empty_tree_fn):
    if is_empty_tree(tree):
        return empty_tree_fn()
    elif isinstance(tree,list) and len(tree)==3:
        #kör kod
        return
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