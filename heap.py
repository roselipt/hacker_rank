# For a heap repreented as array
# parent = floor(i/2)
# left = 2i
# right = 2i +1
#
# REMEMBER that heaps count arrays from 1.
# This is a research project to dig into but I think it has to do 
# with the efficiency of computing 2i and 2i+1.
# (Counting from zero results in some special handling of left and right)

from ctypes import LittleEndianStructure
from re import A


def build_heap(arr):
    '''Takes array of ints, or anything with a <.
    Sorts in place, returning arr, though this is really a reminder.
    MUST REMEMBER that heap sort needs to work with 1-indexed array.'''
    h_size = len(arr)   # Should this be heap_length here?
    for i in reversed(range(1, h_size//2)):
        # convert from zero to one index for array
        max_heapify(arr, i, h_size)
    return arr

def max_heapify(arr, i, heap_size):
    # REMEMBER that i is a one-indexed reference
    # I am curious why heap_size isn't thought of as a parameter here,
    # since it is an essential detail needed from the calling function.
    left = 2*i
    right = 2 *i+1
    
    # if child exists, compare to parent.
    # (less than or EQUAL and the MINUS ONES convert from Heap's 1-index back to Python list's zero-index)
    if left <= heap_size and  arr[i-1] < arr[left-1]:
        greatest = left
    else:
        greatest = i
    if right <= heap_size and arr[greatest-1] < arr[right-1]:
        greatest = right
    if greatest != i:
        arr[i-1], arr[greatest-1] = arr[greatest-1], arr[i-1]
        max_heapify(arr, greatest, heap_size)

def heap_sort(arr):
    build_heap(arr)
    #print(arr, 'after build_heap from sort.')
    #  decrement index, beginning from the end, stopping at 1
    for i in reversed( range(1, len(arr)) ):
        #print('Swap', arr[0], 'heapify', arr[i], 'heap size', i)
        arr[0], arr[i] = arr[i], arr[0]
        heap_size = i    
        max_heapify(arr, 1, heap_size)


a = [4,1,3,2,16,9,10,14,8,7]

print(a)
heap_sort(a)
print(a)
