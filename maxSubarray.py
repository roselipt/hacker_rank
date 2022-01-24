# Maximum Subarray

def maxSubarray(arr):
    '''Given array of integers,
    Returns array of 2 integers.
    First is max subarray. 
    Second is max subsequence.'''
    solution = []
    length = len(arr)
    # Find max subarray
    max_sofar = arr[0]
    # Process arr, for each element, try all subarrays beginning at that element
    for i in range(length):
        # For later, Is there a good way to eliminate the duplication first time through?
        sum_sofar = arr[i]
        max_sofar = max(max_sofar, sum_sofar)
        for j in range(i+1,length):
            sum_sofar += arr[j] 
            max_sofar = max(max_sofar, sum_sofar)
    solution.append(max_sofar)

    # Find max subsequence
    # Generate list of all nonzero length subsequences (defined as subsets)

    def getSubs(l):
        '''Generate all subsets of a list.
        Accepts list,
        Returns list of lists.
        Works recursively, '''
        subsequences = []
        if len(l) == 1:
            return [ [], l ]
        else:
            result = []
            rest = getSubs(l[1:])
            for i in [ [], l[0:1] ]:        # l[0:1] is equivalent to [l[0]]
                for j in rest:
                    result.append( i + j)
            return result
    
    subsets = getSubs(arr)
    # Problem specifies that the empty subset not be considered
    subsets.remove([])
    
    #print(subsets)
    
    sums = [sum(i) for i in subsets]
    print(sums)
    biggestSub = max(sums)
    solution.append(biggestSub)
    
    return solution

a = [-1,2,3,-4,5,10]

answer = maxSubarray(a)
print(answer)