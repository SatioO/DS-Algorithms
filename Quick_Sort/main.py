numbers = [54, 26, 93, 17, 77, 31, 44, 55, 20]


def partition(arr, first, last):
    # 1. setting up initial pivot value
    pivot_value = arr[first]
    # 2. setting up left and right mark
    leftmark = first + 1
    rightmark = last
    # 3. setting up mark to check if partitioning is done or not
    done = False

    while not done:
        # 4. Increment till leftmark is less than pivot value
        while leftmark <= rightmark and arr[leftmark] <= pivot_value:
            leftmark = leftmark + 1

        # 5. Increment till rightmark is greater than pivot value
        while arr[rightmark] >= pivot_value and rightmark >= leftmark:
            rightmark = rightmark - 1

        # 6. check if rightmark has crossed leftmark
        if rightmark < leftmark:
            done = True
        else:
            # 7. swap position of elements
            temp = arr[leftmark]
            arr[leftmark] = arr[rightmark]
            arr[rightmark] = temp

    # 8. replace rightmark with pivot element
    temp = arr[first]
    arr[first] = arr[rightmark]
    arr[rightmark] = temp

    return rightmark


def quick_sort_helper(arr, first, last):
    if first < last:
        partition_value = partition(arr, first, last)
        quick_sort_helper(arr, first, partition_value - 1)
        quick_sort_helper(arr, partition_value + 1, last)

    return arr


def quick_sort(arr):
    sorted_arr = quick_sort_helper(arr, 0, len(numbers) - 1)
    print(sorted_arr)


quick_sort(numbers)