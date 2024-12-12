from tree_algoritms import *
# def empty_tree_fn():
#     return 0

# def leaf_fn(key):
#     return key**2

# def inner_node_fn(key,left_val,right_val):
#     return key+left_val

def traverse(tree,inner_node_fn,leaf_fn,empty_tree_fn):
    if is_empty_tree(tree):
        return empty_tree_fn() #Tomt träd, returnerar en kallelse till funktionen empty_tree_fn
    elif isinstance(tree,list) and len(tree)==3: #Om trädet har rätt struktur, kör detta
        left_tree = left_subtree(tree) #delar upp trädet i vänster och höger
        right_tree = right_subtree(tree)
        key_value = key(tree)
        left = traverse(left_tree,inner_node_fn,leaf_fn,empty_tree_fn) #Rekrusivt går igen trädet för vänster, höger och key
        key_value = traverse(key_value,inner_node_fn,leaf_fn,empty_tree_fn)
        right = traverse(right_tree,inner_node_fn,leaf_fn,empty_tree_fn)
        return inner_node_fn(key_value,left,right)
    elif isinstance(tree,list):
        raise ValueError("felaktig format på listan")
    else:
        return leaf_fn(tree) #Annars är det inte en lista, men har rätt struktur, vilket betyder att det endast finns ett värde. Det är då ett löv. Kallar på leaf_fn för "trädet" som endast är ett värde.

def contains_key(key,tree):
    def leaf_fn(leaf): #Returnerer sant ifall "trädet" vi skickar in är en nyckel. Om det vi skickar in endast är ett värde så är det ett "löv"
        return leaf == key
    
    def inner_node_fn(key,left,right): 
        return left or right or key #Om vänster är ett okej värde, returnera det, annars returnera höger.
    
    def empty_tree_fn(): #Returnerar falskt om trädet är tomt.
        return False
    
    return(traverse(tree,inner_node_fn,leaf_fn,empty_tree_fn))

def tree_size(tree):
    def leaf_fn(key): #returnerar 1 om vi kommit till ett löv
        return 1
    
    def empty_tree_fn(): #Returnerar 0 om trädet är tomt
        return 0

    def inner_node_fn(key,left,right): #Lägger ihop vänster och höger träd samt 1 för den inre noden.
        return 1+left+right
    
    return(traverse(tree,inner_node_fn,leaf_fn,empty_tree_fn)) #Traverserar trädet och räknar antal löv.

def tree_depth(tree):
    def inner_node_fn(key_value, left, right): #Tar 1 för varje inre nod, och lägger till en max av vänster och höger delträd. På så sätt tar den 1+(den största grenen)
        return 1 + max(left, right)

    def leaf_fn(leaf): #Returnerar 1 om det är ett löv
        return 1

    def empty_tree_fn(): #Returnerar 0 om trädet är tomt.
        return 0

    return traverse(tree, inner_node_fn, leaf_fn, empty_tree_fn)

# Test cases

# Contains_key
print(contains_key(6, [6, 7, 8])) # Testar så att den fungerar för vanligta inputs
print(contains_key(2, [6, 7, [[2, 3, 4], 0, []]])) # Testar med en lite mer kompiserad input
print(contains_key(2, [[], 1, 5])) # Testar så den kan returna False
print(contains_key(3, [6, 7, [[2, 3, 4], 0, []]])) # Testar så den kan hitta key i mitten av ett träd och inte bara leafs
print(contains_key(1, [[4, 7, 3], 7, [[2, 3, 4], 0, [3, 7, 2]]])) # Testar så den fungerar för större träd
print(contains_key(1,[])) # Testar så det fungerar för tomma träd

#Tree_size
print(tree_size([2, 7, []])) # Testar så att den fungerar för vanligta inputs
print(tree_size([])) # Testar så det fungerar för tomma träd
print(tree_size([6, 7, [[2, 3, 4], 0, []]])) # Testar så den fungerar för större träd

#Tree_depth
print(tree_depth(9)) # Testar så det fungerar för lätta inputs
print(tree_depth([1, 5, [10, 7, 14]])) # Testar så det fungerar mer större träd
print(tree_depth([6, 7, [[2, 3, 4], 0, []]])) # Testar så den fungerar för mer konmplexa träd
print(tree_depth([])) # Testar så den fungerar för tomma träd

