"""
Interview Question #2

"A palindrome is a string that reads the same forward and backward"

For example: radar or madam

Our task is to design an optimal algorithm for checking whether a given string is palindrome or not!
"""


# My Solution
def is_palindrome(string):
    pointer_1, pointer_2 = 0, len(string) - 1
    while pointer_1 < pointer_2:
        if string[pointer_1] != string[pointer_2]:
            return False
        pointer_1 += 1
        pointer_2 -= 1
    return True


print(is_palindrome("hafnah"))


# Tutor Solution for python, he went on to do a version as above ^^

def palindrome_python(s):
    return s == s[::-1]

print(palindrome_python("hannah"))