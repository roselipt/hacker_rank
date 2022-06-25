class Node :
    def __init__(self, info):
        self.info = info
        self.parent = None
        self.child = None
        self.sibling = None

def entrie(root, s):
    """
    Accepts: r, root of trie
    s, string to be entered
    Returns:
    1 for success
    -1 for failure, meaning string is already present
    
    """
    # Pointer to navigate trie
    p = root
    # Flag to indicate change versus no change to trie
    modified = False
    # Convert sting to list and append None, as all entries in trie must end
    entry = list(s) + [None]   # Same as: entry = list(s).append(None)
    for l in entry:
        #print(l, end = ' ')
        # If next level already exists, advance p and check it.
        if p.child:
            p = p.child
            # Advance p across level until l is found or end is reached.
            while p.info != l and p.sibling:
                p = p.sibling
            # If letter is found (already present) at this level, advance p down a level.
            if p.info == l:
                pass
                #p = p.child
                #print(' {} already in trie, advance p'.format(l, p.info))
            # Letter not found, so add it at this level, and advance p down.
            else:
                p.sibling = Node(l)
                p = p.sibling
                #print(' {} added to existing level'.format(l))
                modified = True
        # Next level does not exist, start it.
        else:
            p.child = Node(l)
            p = p.child
            #print('  {} is first at this level'.format(l))
            #print('    {} != {}'.format(p.info, l))
            #print(type(p.info), type(l))
            modified = True
        #print('  ', l, 'processed, modified is', modified)
    # If entry was made, return 1; else -1 (which can only mean s was already in trie).
    if modified == True:
        return 1
    else:
        return -1
    
                
def traverse_trie(trie):
    pass

# Main

# t to hold root of Trie
t = Node(None)
t.child = Node(None)
#test_words = ['ate','at','bat','cat','bat','abcde']
test_words = ['ate', 'at', 'bat', 'bat', 'abcdef', 'at']
print(test_words)
# print(t)
# print(t.info)
# print(t.child)
# x = t
# print(x, x.child)
for word in test_words:
    print(word, entrie(t, word))
    
print("And if my grandmother had wheels, she'd be a wagon.")
    