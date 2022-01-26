# Enter your code here. Read input from STDIN. Print output to STDOUT
def insertHeap(h, element):
    h.append(element)
    h_size = len(h)
    # MINUS ONES on both these assignments convert to python zero-index
    child = h_size 
    def parent(i):
        '''For i > 1, returns i//2 else -1'''
        if i == 1:
            return -1
        else:
            return i//2

    print(h, 'considering child', child, 'parent', parent(child))
    while child > 1 and h[parent(child)-1] > h[child-1]:
        h[parent(child)-1], h[child-1] = h[child-1], h[parent(child)-1]
        child = parent(child)
            #parent = (child // 2 ) 
        print('now parent', parent(child))
    
def deleteHeap(h, element):
    i = h.index(element) + 1    # PLUS ONE for heap 1-index
    heap_size = len(h)
    parent = i
    left = 2 * parent
    #  As long as left exists
    while left < heap_size:
        # Sift left up into parent
        h[parent-1] = h[left-1]
        parent = left
        left = 2 * parent
    # After loop parent points to last left child
    if parent == i:
        # Element to remove had no left child. (While loop was skipped.)
        h.pop(i-1)
    else:
        # Parent points to last left child, now a duplicate value to be removed
        h.pop(parent-1)

heap = []

def whatsup(i):
    print(i)

for i in reversed(range(2,12,2)):
    print('insert', i)
    insertHeap(heap, i)
print(heap)
deleteHeap(heap, 2)
print(heap)
#for i in arr:
    # INSERT for instructions beginning with 1
    
    # DELETE for instructions beginning with 2
    
    # PRINT MINIMUM for 3
