# open boxes problem
print("open boxes problem")
print("-------------")


def open(box):
    print(box)
    if box == 0:
        return

    open(box - 1)


open(8)


# factorial problem
print("\nfactorial problem")
print("-------------")


def fact(n):
    if n == 0:
        return 1

    return n * fact(n - 1)

# | 1 * fact(0) | -> 1 * 1 -> 1 +
# | 2 * fact(1) | -> 2 *
# | 3 * fact(2) |


print(fact(3))

# sumation
print("\nsumation problem")
print("-------------")


def sum(arr):
    current_index = len(arr) - 1

    if current_index == 0:
        return arr[current_index]

    return arr[current_index] + sum(arr[:current_index])


# 5
# ----
# 3 + sum([5])
# ----
# 10 + sum([5,3])
# ----
# 2 + sum([5,3,10])
# ----

a = [1, 2, 3, 4]
print("\nfinal: {}".format(sum(a)))

# count elements
print("\ncount problem")
print("-------------")


def count(arr, index=0):
    try:
        if arr[index]:
            return count(arr, index + 1)
    except:
        return index


print(count([1, 2, 3, 4]))
# reverse elements
print("\nreverse problem")
print("-------------")


def reverse(arr, start=0, end=0):
    if start > end:
        return arr

    tmp = arr[end]
    arr[end] = arr[start]
    arr[start] = tmp

    return reverse(arr, start + 1, end - 1)


print(reverse([1, 2, 3, 4, 5], 0, 4))

# max num elements
print("\nmax num problem")
print("-------------")


def maxnum(arr, index=0):
    if arr[index] < arr[index + 1]:


print(maxnum([1, 2, 3, 4, 5]))
