from tree_algoritms import *

def traverse(tree,inner_node_fn,leaf_fn,empty_tree_fn):
    if not tree:
        return empty_tree_fn()
    #continue

