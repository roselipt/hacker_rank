#  Complete function:
#  Accepts string of lowercase letters as s.
#  Returns index of any letter whose removal would leave a palindrome, or -1  if no such index exists.

def palindromeIndex(s):
    def isPalindrom(sub):
        '''Recursive palindrome test'''
        # Stopping condition: strings of length 0 or 1 are palindromes.
        if len(sub) <= 1:
            return True
        elif sub[0] == sub[-1]:
            return isPalindrom(sub[1:-1])
        else:
            return False
    
    for i in range(len(s)):
        if isPalindrom(s[0:i]+s[i+1:]):
            return i    
    return -1

# Main

tests = [('bbcb',0), ('bbccb',0), ('bxcb',-1), ('abcd', -1), ('troulylurt', 2), ('troulyylurt', 2)]
for t in tests:
    s, expected = t
    print(s, ', expected, got', expected, palindromeIndex(s))

#print('abcd', isPalindrom('abcd'))
