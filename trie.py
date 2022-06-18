class Node :
    def __init__(self, state):
        self.state = state
        self.parent = None
        self.leftchild = None
        self.rightsib = None

def traverse_trie(trie):
    word = ''
    p = trie
    while p.

test_words = ['at','bat','cat','shat','abcde']

first = Node(None)
first.rightsib = Node('b')
first.rightsib.rightsib = Node('c')

head = first
p = head
while p != None:
    print(p.state, end=' ')
    p = p.rightsib
print()
print('And that is that.')
    