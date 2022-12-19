"""
Interview Question #1

The problem is that we want to reverse a T[] array in O(N) linear time complexity and we want the algorithm to be in-place as well - so no additional memory can be used!

For example: input is [1,2,3,4,5] then the output is [5,4,3,2,1]

"""


##MY VERSION
def reverse(arr):
    pointer_1 = 0
    pointer_2 = len(arr) - 1
    while pointer_1 < pointer_2:
        temp = arr[pointer_1]
        arr[pointer_1] = arr[pointer_2]
        arr[pointer_2] = temp
        pointer_1 += 1
        pointer_2 -= 1
    return arr


print(reverse([1, 2, 3, 4, 5]))

## TUTOR'S VERSION
"""

def reverse(nums):

    # pointing to the first item
    start_index = 0
    # index pointing to the last item
    end_index = len(nums)-1

    while end_index > start_index:
        # keep swapping the items
        nums[start_index], nums[end_index] = nums[end_index], nums[start_index]
        start_index = start_index + 1
        end_index = end_index - 1


if __name__ == '__main__':

    n = [-3, 0, 3]
    reverse(n)
    print(n)

"""