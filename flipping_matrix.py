
def max_flipping(arr):
    """
    Accepts q, 2n X 2n arrays.
    Rules allow unlimited flipping of rows or columns.
    Return max possible sum of the upper left quadrant, for each of q arrays. 
    """
    # The key realization is that each value in first quadrant may be switched ONLY with one other
    # corresponding value in EACH of the other three quadrants.
    # For this implentation, I imagined finding each location from its outside corner.

    answers = []
    # Process each matrix in arr
    for m in arr:
        answer = 0  
        # Get n and process upper left quadrant
        n = len(m)//2       # Does this belong here? Remember to check problem specs. (Does n change?)
        for r in range(n):
            for c in range(n):
                max = m[r][c]
                # Calculate positions of three values that could flip into this position.
                # Upper left, lower left, lower right
                others = [ (r, (2*n-1)-c), \
                           ((2*n-1)-r, (2*n-1)-c), \
                           ((2*n-1)-r, c) ]
                for location in others:
                    row, col = location
                    if m[row][col] > max:
                        max = m[row][col]
                answer += max
        answers.append(answer)
    # print('row, column test')
    # print("(2,0) in a1 should be 9:", arr[0][2][0])
    # print("(2,0) in a2 should be 11:", arr[1][2][0])
    return answers


# Main
#test = [ [[1],[2],[3],[4]], \
test = [ [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]], \
         [[1,2,3,4], [5,6,7,8], [11,10,9,12], [13,14,15,16]]  \
        ]
for t in test:
    for row in t:
        print(row)
    print()
print('Expecting 54 and 53 got', max_flipping(test))