"""
Function Description

Complete the function twoStrings in the editor below. It should return a string, either YES or NO based on whether the strings share a common substring.

twoStrings has the following parameter(s):

s1, s2: two strings to analyze .
"""

def check(s1, s2):
    interc = set(list(s1)).intersection(set(list(s2)))

    return 'YES' if len(interc) else 'NO'

if __name__=='__main__':

    inpt = int(input())
    for ipt in range(inpt):
        s1,s2 = input(),input()
        result = check(s1, s2)
        print(result)