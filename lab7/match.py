import books

def match(seq, pattern):
    """
    Returns whether given sequence matches the given pattern
    """
    if not pattern:
        return not seq
    elif pattern[0] == '--':
        if match(seq, pattern[1:]):
            return True
        elif not seq:
            return False
        else:
            return match(seq[1:], pattern)
    elif not seq:
        return False
    elif isinstance(pattern[0],list):
        return match(seq[0],pattern[0]) and match(seq[1:],pattern[1:])
    elif pattern[0] == '&':
        return match(seq[1:], pattern[1:])
    elif seq[0] == pattern[0]:
        return match(seq[1:], pattern[1:])
    else:
        return False
    
def search(pattern,db):
    result=[]
    for data in db:
        if match(data,pattern):
            result.append(data)
    return result
            

print(search([],books.db))