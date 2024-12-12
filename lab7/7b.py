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
        key_value = key(tree) #Tilldelar key value genom att kalla på funktionen key.
        left = traverse(left_tree,inner_node_fn,leaf_fn,empty_tree_fn) #traverserar vänster del av trädet
        right = traverse(right_tree,inner_node_fn,leaf_fn,empty_tree_fn) # traverserar höger del av trädet
        return inner_node_fn(key_value,left,right) #returnerar inre noden genom att kalla på inner node fn. Den 
    elif isinstance(tree,list): #Om trädet är en lista men fel struktur så funkar det inte, kastar då valueerror.
        raise ValueError("felaktig format på listan")
    else:
        return leaf_fn(tree) #Annars är det inte en lista, men har rätt struktur, vilket betyder att det endast finns ett värde. Det är då ett löv. Kallar på leaf_fn för "trädet" som endast är ett värde.

def contains_key(key,tree):
    def leaf_fn(leaf): #Returnerer sant ifall "trädet" vi skickar in är en nyckel. Om det vi skickar in endast är ett värde så är det ett "löv"
        return leaf == key
    
    def inner_node_fn(key,left,right): 
        return left or right #Om vänster är ett okej värde, returnera det, annars returnera höger.
    
    def empty_tree_fn(): #Returnerar falskt om trädet är tomt.
        return False
    
    return(traverse(tree,inner_node_fn,leaf_fn(key),empty_tree_fn)) #Kallar på traverse med sina egna funktioner för contains key.

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