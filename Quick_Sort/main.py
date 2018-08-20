numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]

#               |                       |


# rules
# select first element as pivot
# initialize leftmark -> 0, rightmark -> length of array - 1
# check if leftmark is greater than pivot_value
# check if rightmark is less than pivot_value
def partition(arr, first, last):
    # 1. setting a initial pivot value
    pivot_value = arr[first]
    # 2. choose left and right mark
    leftmark = first + 1
    rightmark = last

    done = False

    while not done:
        while leftmark <= rightmark and arr[leftmark] <= pivot_value:
            leftmark = leftmark + 1

        while arr[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


def quick_sort_helper(arr, first, last):
    if first < last:
        partition_value = partition(arr, first, last)
        quick_sort_helper(arr, first, partition_value - 1)
        quick_sort_helper(arr, partition_value + 1, last)


def quick_sort(num):
    quick_sort_helper(num, 0, len(num) - 1)


quick_sort(numbers)