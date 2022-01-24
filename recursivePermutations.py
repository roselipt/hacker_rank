#  Recursive permution functions.

from unittest import result


def reverseList(l):
    if len(l) == 1:
        return l
    else:
        return [l[0]] + reverseList(l[1:])

def subsets(seq):
    # The key to this when I came back to it is imagining the building of the possible
    # permutations from right to left.
    if len(seq) == 1:
        return [ [], seq]
    else:
        result = []
        the_rest = subsets(seq[1:])
        # BIG WOWSA for me!!        seq[0:1] is a MAYBE BETTER BUT EQUIVALENT way to write [ seq[0] ]
        for i in [ [], seq[0:1] ]:
            for j in the_rest: 
                #print(i, j, i+j)
                result.append(i+j)
        return result

# How about an iterative creation of subset?
def subsets_it(seq):
    #result = []
    length = len(seq)
    
    # Generate a list of tuples: each element and the empty list for omitting that element
    bin_seq = []
    for i in seq[1:]:
        bin_seq.append( (i, []))

    # Starting 'result' list is the first element and the empty list, 
    # representing on,off for first item.
    result = [ [seq[0]], [] ]
    for i in seq[1:]:
        new_result = []
        (on, off) = ([i], [])
        for i in (on,off):
            for j in range(len(result)):
                new_result.append(result[j] + i)
        #print(new_result)
        result = new_result
    print('And, scene.')
        
    return result


a = [0,1,2,3,4,5,6,7,8,9]
b = [1,2,3]

print(reverseList(a))
print('recursive:', subsets(b))
print('iterative:', subsets_it(b))