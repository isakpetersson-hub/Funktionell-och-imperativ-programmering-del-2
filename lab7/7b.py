from tree_algoritms import *
# def empty_tree_fn():
#     return 0

# def leaf_fn(key):
#     return key**2

# def inner_node_fn(key,left_val,right_val):
#     return key+left_val

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

def contains_key(key,tree):
    def leaf_fn(key):
        def leaf_compare(tree):
            return tree == key
        return leaf_compare
    
    def inner_node_fn(key,left,right):
        return left or right
    
    def empty_tree_fn():
        return False
    
    return(traverse(tree,inner_node_fn,leaf_fn(key),empty_tree_fn))

def tree_size(tree):
    def leaf_fn(key):
        return 1
    
    def empty_tree_fn():
        return 0

    def inner_node_fn(key,left,right):
        return 1+left+right
    
    return(traverse(tree,inner_node_fn,leaf_fn,empty_tree_fn))

def tree_depth(tree):
    def inner_node_fn(key_value, left, right):
        return 1 + max(left, right)

    def leaf_fn(leaf):
        return 1

    def empty_tree_fn():
        return 0

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)