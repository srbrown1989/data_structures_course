"""
Interview Question #3

Our task is to design an efficient algorithm to reverse a given integer.
For example if the input of the algorithm is 1234
then the output should be 4321.

"""


# My Solution
def reverse(i):
    i = str(i)
    return int(i[::-1])


print(reverse(12340))

# Tutor solution
"""
def reverse_integer(n):

    reversed_integer = 0

    while n > 0:
        remainder = n % 10
        reversed_integer = reversed_integer*10 + remainder
        n = n // 10

    return reversed_integer


if __name__ == '__main__':
    print(reverse_integer(12345678))

"""