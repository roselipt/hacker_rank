#  Recursive palindrome test for strings plus code to test

def isPalindrome(s):
    '''Assumes string, returns boolean'''
    length = len(s)
    if length == 0 or length == 1:
        return True
    # For string of length 2 or more, test first and last
    elif s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    
    else:
        return False

def oneOff(s):
    '''Assumes string, determines if string can be made palindrome by removing one character.
    If so it returns int, the position of that character.
    If not, returns -1.
    '''
    if isPalindrome(s):
        return 'already is!'
    else:
        for i in range(len(s)):
            n = s[0:i] + s[i+1:]
            #print('checking i =', i, 'n =', n, isPalindrome(n))
            if isPalindrome(n):
                return i
        return -1

tests = ['aaaab', 'a', 'ab', 'abcba', 'abcdefgfedcba', 'abcddcba', 'abcdef']
print('Tests!')
for t in tests:
    result = str(oneOff(t)).ljust(4)
    t = t.ljust(10)
    print(t, result)
# testee = [ \
#     'aa',    \
#     'abba',\
#     '',      \
#     'x',     \
#     'ab',    \
#     'abced', \
#     'abccbad',\
#     'abcdecba'\
#     ]

# for t in testee:
#     print(t.ljust(10), str(isPalindrome(t)).ljust(6))