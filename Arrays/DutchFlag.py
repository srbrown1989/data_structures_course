##My solution, based on Pseudocode Given.
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]
    return arr


def national_flag(arr, mid):
    i, j, k = 0, 0, len(arr) - 1

    while j <= k:
        if arr[j] < mid:
            arr = swap(arr, i, j)
            i += 1
            j += 1
        elif arr[j] > mid:
            arr = swap(arr, j, k)
            k -= 1
        else:
            j += 1
    return arr


if __name__ == "__main__":
    MID_VALUE = 1
    data = [1, 2, 0, 0, 1, 2, 0, 0, 1, 1, 2, 2, 0, 0]

    print(national_flag(data, MID_VALUE))

"""
Tutor's Solution


"""