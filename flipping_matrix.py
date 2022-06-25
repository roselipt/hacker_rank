
def max_flipping(arr):
    """
    Accepts q, 2n X 2n arrays.
    Rules allow unlimited flipping of rows or columns.
    Return max possible sum of the upper left quadrant, for each of q arrays. 
    """
    answer = []
    for a in arr:
        n = len(a)//2
        # Upper left quadrant is (r,c)
        print(n)
        print(a[0])
    print('row, column test')
    print("(2,0) in a1 should be 9:", arr[0][2][0])
    print("(2,0) in a2 should be 11:", arr[1][2][0])
    return answer


# Main
#test = [ [[1],[2],[3],[4]], \
test = [ [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], \
         [[1,2,3,4], [5,6,7,8], [11,10,9,12]], [13,14,15,16] \
        ]
print(max_flipping(test))